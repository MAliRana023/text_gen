import streamlit as st
from transformers import pipeline
1
# Load the text generation pipeline
text_generator = pipeline("text-generation")

# Define the Streamlit app
def main():
    # Set the title and description of the app
    st.title("Blog Post Generator")
    st.write("Enter a blog title and click the button to generate a blog post.")

    # Get user input for the blog title
    blog_title = st.text_input("Enter the blog title:", "How to Improve Your Writing Skills")

    # Generate the blog post on button click
    if st.button("Generate Blog Post"):
        if blog_title:
            # Generate the blog post based on the title
            blog_post = text_generator(blog_title, max_length=500, num_return_sequences=1)[0]['generated_text']

            # Display the generated blog post
            st.subheader("Generated Blog Post:")
            st.write(blog_post)
        else:
            st.warning("Please enter a blog title.")

if __name__ == "__main__":
    main()
