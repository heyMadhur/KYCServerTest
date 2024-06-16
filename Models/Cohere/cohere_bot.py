import cohere


api_token= "xtoMjbTi2JOblqHNeibEDIJV0mjHMeOshZJSLZ27"

co = cohere.Client(
    api_key=api_token,
)

def agent_cohere(ingredients):
    context= "You are a Strict Dietician. You will be given a list of nutrients name and their percentage in a packaged food. Based on that identify which nutrients are good and which are bad and give a number from 1 to 100 based on how healthy the food is. Greater Number means healthy food. IMPORTANT: Answer Strictly in given JSON Format: { Score: 'Score from 1 to 100', Nutrients with Sufficient Quantity: [List of nutrients], Nutrients less than Sufficient Quantity: [List of Nutrients], Nutrients with Excessive Quantity: {List of Nutrients] }"

    chat = co.chat(
        message=(context+ingredients),
        # message= "What are latest AI Achievements this month",
        model="command-r-plus"
    )



    response= chat.text.strip('\n')
    # print(response)
    split_string= response.split("Explanation",1)
    response= split_string[0].strip()
    explanation= "Explanation" + split_string[1].strip()
    # response= chat.text.strip('\n')
    return response, explanation





