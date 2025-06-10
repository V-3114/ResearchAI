from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver import DriverManager
import time

def ask_gpt_ai(driver, wait, prompt_text):
    
    start_time = time.time()  # Start timer

    try:
        # Open ChatGPT
        driver.get("https://chatgpt.com/")

        # Locate text input
        editable_div = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @id="prompt-textarea"]'))
        )
        editable_div.send_keys(prompt_text)
        time.sleep(3)
        editable_div.send_keys(Keys.ENTER)

        # Wait for AI response to appear
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Copy"]'))
        )
        time.sleep(2)
        #print("ready to copy")
        # Collect and join all response texts
        response_parts = driver.find_elements(By.XPATH, '//div[@class="markdown prose dark:prose-invert w-full break-words dark"]')
        print(response_parts)
        response_texts = [part.text.strip() for part in response_parts if part.text.strip()]
        full_response = "\n\n".join(response_texts)

    except Exception as e:
        return f"⚠️ An error occurred: {e}"

    elapsed_time = time.time() - start_time  # End timer
    print(f"\n⏱️ Time taken: {elapsed_time:.2f} seconds")

    return full_response

if __name__ == "__main__":
    # Step 1: Setup
    manager = DriverManager(headless=True)

    # Step 2: Get driver and wait objects
    driver, wait = manager.get_driver()
    file_path = r'C:\Users\V\Documents\Python\ResearchAI\backend\prompts.txt'
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

        print(text)
    while True:
        # Get user input
        user = input(">")
        if user != 'quit':

            #Prompt engineering

            History = ''
            prompt1 = "You're a UX Reserach assistant. You have decades of research experience in the field. Your ability to help junior researchers understand the concepts  and teach them by breaking process down simply and inuitively and planning and conducting research, and to aid your research peers by providing equal value and respecting their work of process and idealogies and ideas, make you an excellent researcher along with an outstanding mentor. Now people come to you often regarding a research they are planning to conduct and need either your guidance as a mentor throughout the process or a peer they can work freely with, who can work with them, respect their methods and process, while aiding in areas they seek assistance. Your responses are short and guiding. Do not acknowledge background and begun your response, responding to what's user input is."
            prompt = f'Background: {prompt1}                  User Input: {user}'

            #generate and output response
            response_gpt = ask_gpt_ai(driver, wait, prompt)
            print("\n🧠 ChatGPT Response:\n", response_gpt)
        else:
            print('break')
            manager.quit_driver()
            break
