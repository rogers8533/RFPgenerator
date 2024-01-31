import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "API KEY HERE"


def generate_response(prompt, max_tokens=350):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()


def transform_response(response, transformation_type):
    prompt = f"Transform: {transformation_type}\nText: {response}\nTransformed:"
    transformed_response = generate_response(prompt, max_tokens=100)
    return transformed_response


def main():
    st.title("Portfolio RFP Generator")

    # User inputs
    portfolio_text = st.text_area("Enter your portfolio:", height=10)
    portfolio_type = st.selectbox("Select portfolio type:", ["Conservative", "Moderate", "Aggressive"])
    rfp_question = st.text_input("Enter your RFP question:")

    if st.button("Generate Response"):
        prompt = f"Portfolio: {portfolio_text}\nType: {portfolio_type}\nQuestion: {rfp_question}\nResponse:"
        generated_response = generate_response(prompt)
        st.text_area("Generated Response:", value=generated_response, height=200)

    # Transformation buttons
    transformation_types = ["Passive voice to Active voice", "Make it Plain", "Make More Readable", "Elaborate",
                            "Concise"]
    selected_transformation = st.selectbox("Select a transformation:", transformation_types)

    if st.button("Apply Transformation"):
        transformed_response = transform_response(generated_response, selected_transformation)
        st.text_area(f"{selected_transformation}:", value=transformed_response, height=200)


if __name__ == "__main__":
    main()
