import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Pro Resume & CV Architect", page_icon="📄")

# Sidebar API KEY
st.sidebar.title("Konfigurasi")
api_key = st.sidebar.text_input("Masukkan Gemini API Key", type="password")

if api_key:
    
    genai.configure(api_key=api_key)

    # Gunakan model yang stabil
    model = genai.GenerativeModel("gemini-1.5-flash")

    st.title("📄 Pro Resume & CV Architect")
    st.markdown("---")
    st.caption("Asisten AI untuk menyusun Resume Profesional & ATS-Friendly")

    # Input User
    job_desc = st.text_area(
        "Tempel Deskripsi Pekerjaan Target:",
        placeholder="Contoh: Membutuhkan Skill Python, Data Analysis..."
    )

    user_experience = st.text_area(
        "Tempel Pengalaman/Skill Kamu Saat Ini:",
        placeholder="Contoh: Saya pernah bekerja sebagai admin selama 2 tahun..."
    )

    if st.button("Buat Draft Resume"):

        if job_desc and user_experience:

            with st.spinner("Sedang merancang resume terbaik untukmu..."):

                prompt = f"""
                Kamu adalah seorang Expert HR dan CV Writer.

                Buatkan Resume ATS-Friendly berdasarkan data berikut:

                Target Job:
                {job_desc}

                User Experience:
                {user_experience}

                Instruksi:
                - Gunakan action verbs
                - Masukkan keyword penting dari job description
                - Buat summary profesional
                - Format markdown rapi
                """

                response = model.generate_content(prompt)

                st.subheader("Hasil Draft Resume:")
                st.markdown(response.text)

                st.download_button(
                    "Download Draft (TXT)",
                    response.text,
                    file_name="draft_resume.txt"
                )

        else:
            st.warning("Mohon isi deskripsi pekerjaan dan pengalaman terlebih dahulu.")

else:
    st.info("Masukkan Gemini API Key di sidebar untuk memulai.")
