import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

# -------- Load external CSS --------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("css/style.css")   # 👈 loading your css file

# -------- Helper(s) --------
def load_lottie_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottie_animation(
    "https://lottie.host/2cc877db-c95f-4ff9-bc7a-1ec0bf17a7a1/VOg9oU9vRB.json"
)
lottie_connect = load_lottie_animation(
    "https://lottie.host/d7a9c624-ab6e-48ee-aaa1-ebe52021f863/9dIHXLfCDQ.json"
)

# ================== SECTIONS ==================

# -------- Navbar --------
st.markdown("""
<div class="navbar">
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#experience">Experience</a>
    <a class="nav-link" href="#projects">Projects</a>
    <a class="nav-link" href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---- ABOUT ----
st.markdown("<span id='about'></span>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns((1,1))
    with col1:
        st.subheader("👋 Hi, I’m Ankit Kumar")
        st.title("Software Engineer | Full-Stack Developer | Cloud Enthusiast")
        st.write("""
I’m a developer passionate about building **scalable backend systems**,  
**cloud-native applications**, and tools that solve real-world problems.  

Currently working at Syscloud, I specialize in **microservices, distributed systems, and cloud security**.
        """)
        st.write("🌐 LinkedIn: [linkedin.com/in/ankit-kumar-085365163](https://www.linkedin.com/in/ankit-kumar-085365163/)")
        st.write("💻 GitHub: [github.com/swayamsivam37](https://github.com/swayamsivam37)")
    with col2:
        st_lottie(lottie_coder, height=280)

st.write("---")

# ---- EXPERIENCE & EDUCATION ----
st.markdown("<span id='experience'></span>", unsafe_allow_html=True)
with st.container():
    col3, col4 = st.columns((1,1))
    with col3:
        st.subheader("🎓 Education")
        st.write("**B.Tech in Computer Science & Engineering**")
        st.write("Lovely Professional University, Phagwara (2017 – 2021)")
        st.write("CGPA: 8.75/10")

    with col4:
        st.subheader("💼 Experience")

        st.write("**Senior Software Engineer – Syscloud Tech, Hyderabad** (2023 – Present)")
        st.markdown("""
- Built **SMV3 secure package** (Node.js + PHP) for secret management.  
- Designed **Action Link with Expiry (ALEX)** framework, used company-wide.  
- Boosted backup & restore performance by **100x** via microservices.  
        """)

        st.write("**Software Engineer – Syscloud Tech, Hyderabad** (2021 – 2023)")
        st.markdown("""
- Rewrote restore/export pipeline → **80x faster**.  
- Developed **cloudmover service** (Node.js, AWS S3, Lustre FS) → **200x faster**.  
- Built **Job Manager (AWS SQS)** for decoupled workflows.  
        """)

        st.write("**Intern – Syscloud Tech, Hyderabad** (2020 – 2021)")
        st.markdown("""
- Built **real-time monitoring alerts** (AWS Lambda + MS SQL).  
- Implemented **structured logging (Monologger)** in PHP.  
- Created **CloudWatch dashboards** for workload tracking.  
        """)

st.write("---")

# ---- PROJECTS ----
st.markdown("<span id='projects'></span>", unsafe_allow_html=True)
st.header("🚀 My Projects")

# ---- Project 1 ----
with st.container():
    col_img, col_details = st.columns((1,2))
    with col_img:
        st.image("Images/resume-analyzer.jpg", use_container_width=False)
    with col_details:
        st.subheader("AI-Powered Resume Analyzer")
        st.write(
            "Streamlit-based web app that provides AI-powered feedback on your resume. "
            "Upload a PDF or TXT resume and get structured analysis to improve it for your job role."
        )
        st.write("**Tech stack:** Streamlit, OpenAI API, Python")
        st.markdown("[🌐 Live App](https://ai-resume-analyzer-new.streamlit.app/) | "
                    "[💻 GitHub Repo](https://github.com/swayamsivam37/AI-Resume-Analyzer)")

st.write("")

# ---- Project 2 (copy for now) ----
with st.container():
    col_img, col_details = st.columns((1,2))
    with col_img:
        st.image("Images/resume-analyzer.jpg", caption="", use_container_width=False)
    with col_details:
        st.subheader("AI-Powered Resume Analyzer (Copy)")
        st.write(
            "Another showcase of the same project card layout. "
            "You can replace this with your next project while keeping the design consistent."
        )
        st.write("**Tech stack:** Streamlit, OpenAI API, Python")
        st.markdown("[🌐 Live App](https://ai-resume-analyzer-new.streamlit.app/) | "
                    "[💻 GitHub Repo](https://github.com/swayamsivam37/AI-Resume-Analyzer)")

st.write("---")

# ---- CONTACT ----
st.markdown("<span id='contact'></span>", unsafe_allow_html=True)
with st.container():
    st.subheader("📬 Get in Touch")

    # Contact form
    contact_form = """
    <form action="https://formsubmit.co/swayam.sivam37@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_connect, height=300)

