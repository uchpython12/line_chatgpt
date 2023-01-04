import openai
import Line_API
# openai_gpt回傳
def chat_gpt(prompt):
    """-----------------------------需要改成自己的--------------------------------"""
    auth_token, 接收人的id,openai_key = Line_API.Line_讀取設定檔Excel('line.xlsx')
    # openai.api_key = ''
    openai.api_key = openai_key
    """-----------------------------需要改成自己的--------------------------------"""
    response = openai.Completion.create(
        engine = "text-davinci-003",    # select model
        prompt = prompt,
        max_tokens = 512,               # response tokens
        temperature = 1,                # diversity related
        top_p = 0.75,                   # diversity related
        n = 1,                          # num of response
    )

    completed_text = response["choices"][0]["text"]
    print(completed_text)
    return completed_text