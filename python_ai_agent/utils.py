import google.generativeai as genai
import os # API 키를 환경 변수로 관리하기 위해 os 모듈 import 추가


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") # 환경 변수에서 API 키를 가져옵니다.
genai.configure(api_key=GOOGLE_API_KEY) # Gemini API 키 설정


def llm_call(prompt: str, model: str = "gemini-pro") -> str: # 모델 이름 변경
    generative_model = genai.GenerativeModel(model) # Gemini 모델 로드
    response = generative_model.generate_content(prompt) # Gemini API 호출
    return response.text # Gemini API 응답에서 텍스트 추출

async def llm_call_async(prompt: str, model: str = "gemini-pro") -> str: # 모델 이름 변경
    generative_model = genai.GenerativeModel(model) # Gemini 모델 로드
    response = await generative_model.generate_content_async(prompt) # Gemini 비동기 API 호출
    print(model,"완료")
    return response.text # Gemini API 응답에서 텍스트 추출

if __name__ == "__main__":
    test = llm_call("안녕")
    print(test)

