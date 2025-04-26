# nlp_interface/gemini_client.py
import os
import openai

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        openai.api_key = self.api_key

    def ask_gemini(self, prompt: str) -> str:
        """
        Send a prompt to Gemini API and return the response.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant helping to control a robot."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=100
            )
            return response['choices'][0]['message']['content'].strip()

        except Exception as e:
            print(f"[GeminiClient] Error: {e}")
            return "Sorry, I couldn't process that command."

