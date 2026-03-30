import streamlit as st

st.set_page_config(page_title="AI Job Assistant", layout="centered")

st.title("🚀 AI Job Application Assistant")
st.write("Paste a job description and generate optimized content instantly.")

job_desc = st.text_area("📄 Job Description", height=200)

if st.button("Generate"):
    if job_desc:
        st.subheader("✅ Optimized Summary")
        st.write(
            "Experienced Full Stack Developer with expertise in cloud, APIs, and scalable systems aligned with the job requirements."
        )

        st.subheader("🛠 Matching Skills")
        st.write("Python, AWS, React, SQL, REST APIs, Azure, Data Engineering")

        st.subheader("💡 Suggested Answer")
        st.write(
            "I am highly interested in this role because my experience aligns closely with your requirements, particularly in building scalable systems and working with cloud technologies."
        )
    else:
        st.warning("Please paste a job description.")
