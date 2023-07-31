# Automated Service Tool

The Automated Service Tool is an ongoing project aimed at creating a chatbot-based customer service tool for the electronic accessories store "Protech." The goal is to leverage the power of the GPT-3.5 language model from OpenAI to deliver personalized and efficient customer support tailored to different types of customers.

## Expected Features

The key features we aim to implement in the Automated Service Tool include:

- **Intelligent Chatbot**: The core of the tool will be a chatbot powered by the advanced GPT-3.5 language model. This intelligent chatbot will be capable of understanding and responding to various customer queries effectively.

- **Customer Segmentation**: To provide a more tailored experience, the chatbot will be designed to recognize and categorize customers into three main types:

  1. New Customer: The chatbot will greet and engage new customers with detailed and informative responses, assisting them in exploring the wide range of products and services available at Protech.

  2. Returning Customer: For returning customers, the chatbot will prioritize quick and efficient responses. It will be equipped to address queries related to previous purchases and promptly resolve any potential issues they might encounter.

  3. Customer with Uncompleted Order: In cases where a customer has an uncompleted order, the chatbot will provide additional product information, answer any specific questions, and guide the customer through the checkout process, ensuring a smooth and convenient shopping experience.

- **Seamless Integration**: The chatbot will be seamlessly integrated into the Protech store website. Customers will be able to access the chatbot conveniently from the website's support section, enhancing their overall shopping experience.

## Getting Started

As the project is still under development, there are no executable steps at the moment. However, once the project reaches a stable state, the following steps will guide users in setting up and running the Automated Service Tool:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/Automated-Service-Tool.git
   cd Automated-Service-Tool
   ```

2. Install the required dependencies:

   ```
   pip install openai  # Install the OpenAI Python library
   ```

3. Obtain the API Key:

   - Sign up for an account at OpenAI (https://openai.com/) if you haven't already.
   - Create an API key and save it securely in a text file, e.g., `api_key.txt`. Make sure the file contains only the API key without any extra spaces or characters.

4. Customize the Chatbot Configuration:

   - Open `main.py` and update the path to the `api_key.txt` file in the `obter_api_key` function.
   - Customize the prompts for each customer type in the `atendimento_ao_cliente` function.

5. Run the Chatbot:

   ```
   python main.py
   ```

## Contribution

We welcome contributions to this project. If you are interested in making the Automated Service Tool even better, feel free to open issues or submit pull requests on GitHub.

## Acknowledgments

- The Automated Service Tool utilizes the GPT-3.5 language model provided by OpenAI.

## Contact

For any questions, feedback, or inquiries regarding this project, please feel free to contact us via the following channels:

- Email: verissimo.eduardo@unifesp.br
- Email: raphael.damasceno@unifesp.br

---
*Note: The images used in this README are for illustrative purposes only and should be replaced with actual logos and screenshots of the project.*
