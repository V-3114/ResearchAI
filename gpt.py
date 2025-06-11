from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver import DriverManager
import time

def ask_gpt_ai(user_input):
    
    start_time = time.time()  # Start timer


    print("got the driver")
    personality = [
    "You are an excelletnt User Experience Research assistant, with decades of experience in planning and conducting user research across various team sizes.",
    ]

    RULES = [
    "Your responses should be encouraging and leading for sparking ideas in user.",
    "Keep your responses short and and only expand on your response, if it's relevant to the user query.",
    "Only respond to user input and do not acknowledge personality or rules.",
    "Help user conduct research by offering UXR frameworks"
    ]

    chat_history = []
    #-------------------------------------------------------

    manager = DriverManager(headless=False)
    driver, wait = manager.get_driver()

    prompt_style = personality[0]
    rules_text = "\n".join([f"- {rule}" for rule in RULES])
    chat_history.append(f"User: {user_input}")
    history_text = "\n".join(chat_history)  # Last 4 query:response

    prompt_text = (
        f"{prompt_style}\n\n"
        "Follow these rules when answering:\n"
        f"{rules_text}\n\n"
        f"{history_text}\n"
        )

    #-------------------------------------------------------

    try:
        # Open ChatGPT
        driver.get("https://chatgpt.com/")
        print("opened link")

        # Locate text input
        editable_div = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @id="prompt-textarea"]'))
        )
        print("page loaded")
        time.sleep(2)
        lines = prompt_text.split('\n')
        for i, line in enumerate(lines):
            editable_div.send_keys(line)
            if i < len(lines) - 1:
                editable_div.send_keys(Keys.SHIFT, Keys.ENTER)
        print("entered text")
        time.sleep(2)
        editable_div.send_keys(Keys.ENTER)
        print("enter")
        time.sleep(2)
        # Wait for AI response to appear
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Copy"]'))
        )
        time.sleep(2)
        # Collect and join all response texts
        response_parts = driver.find_elements(By.XPATH, '//div[@class="markdown prose dark:prose-invert w-full break-words dark"]')
        response_texts = [part.text.strip() for part in response_parts if part.text.strip()]
        full_response = "\n\n".join(response_texts)

        chat_history.append(f"GPT: {full_response}")

        print(full_response)
        manager.quit_driver

        elapsed_time = time.time() - start_time  # End timer
        print(f"\n⏱️ Time taken: {elapsed_time:.2f} seconds")
            
    except Exception as e:
        elapsed_time = time.time() - start_time  # End timer
        print(f"\n⏱️ Time taken: {elapsed_time:.2f} seconds")
        return f"⚠️ An error occurred: {e}"
