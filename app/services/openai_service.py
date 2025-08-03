

from app.config import settings
import openai
try:
	from openai import OpenAI
	_has_client = True
except ImportError:
	_has_client = False

class OpenAIService:
	def __init__(self):
		self.api_key = settings.openai_api_key
		openai.api_key = self.api_key
		self.model = "gpt-4o-mini"  # modelo padrão fixo
		if _has_client:
			self.client = OpenAI(api_key=self.api_key)

	async def generate_markdown(self, transcription_text: str, prompt: str, use_client: bool = False, model: str = None) -> str:
		"""
		Envia a transcrição e o prompt para o modelo OpenAI (gpt-4o-mini por padrão) e retorna o markdown gerado.
		Se use_client=True, utiliza a interface nova (OpenAI client), senão usa a interface padrão async.
		"""
		system_prompt = prompt or settings.openai_transcribe_prompt
		messages = [
			{"role": "system", "content": system_prompt},
			{"role": "user", "content": transcription_text}
		]
		model_name = model or self.model
		try:
			if _has_client:
				# O método 'create' é síncrono, não deve ser usado com 'await'.
				completion = self.client.chat.completions.create(
					model=model_name,
					messages=messages,
					temperature=0.2,
					max_tokens=4096,
					response_format={"type": "text"}
				)
				markdown = completion.choices[0].message.content
				return markdown
			else:
				raise RuntimeError("OpenAI client não disponível. Atualize o pacote openai.")
		except Exception as e:
			raise RuntimeError(f"Erro ao gerar markdown via OpenAI: {e}")
