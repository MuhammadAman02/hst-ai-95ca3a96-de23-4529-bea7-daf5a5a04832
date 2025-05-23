"""
AI Engineer Portfolio - NiceGUI Implementation
"""
from nicegui import ui, app
import logging
from app.core.config import settings
from app.services.portfolio_service import PortfolioService
import os

logger = logging.getLogger(__name__)

# Initialize the portfolio service
portfolio_service = PortfolioService()

# Configure NiceGUI app
app.title = settings.APP_NAME
app.favicon = "💻"

# Add static files directory for images, CSS, etc.
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
if os.path.exists(static_dir):
    app.add_static_files('/static', static_dir)
    logger.info(f"Serving static files from {static_dir}")
else:
    os.makedirs(static_dir, exist_ok=True)
    logger.info(f"Created static directory at {static_dir}")

# Add custom CSS
with ui.head():
    ui.html("""
    <style>
        :root {
            --primary: #4F46E5;
            --primary-dark: #4338CA;
            --secondary: #10B981;
            --dark: #1F2937;
            --light: #F9FAFB;
            --gray: #6B7280;
            --light-gray: #E5E7EB;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', sans-serif;
            color: var(--dark);
            background-color: var(--light);
            line-height: 1.6;
        }
        
        .section {
            padding: 2rem 0;
            border-bottom: 1px solid var(--light-gray);
        }
        
        .section:last-child {
            border-bottom: none;
        }
        
        .card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .skill-tag {
            background-color: var(--light-gray);
            color: var(--dark);
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 500;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            display: inline-block;
        }
        
        .nav-link {
            color: var(--dark);
            font-weight: 500;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            transition: background-color 0.2s ease;
        }
        
        .nav-link:hover {
            background-color: var(--light-gray);
        }
        
        .social-icon {
            color: var(--gray);
            font-size: 1.5rem;
            margin-right: 1rem;
            transition: color 0.2s ease;
        }
        
        .social-icon:hover {
            color: var(--primary);
        }
        
        .hero-section {
            background: linear-gradient(135deg, #4F46E5 0%, #10B981 100%);
            color: white;
            padding: 3rem 0;
        }
        
        .project-image {
            border-radius: 0.5rem;
            overflow: hidden;
        }
        
        .timeline-item {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 2rem;
        }
        
        .timeline-item:before {
            content: '';
            position: absolute;
            left: 0;
            top: 0.25rem;
            width: 1rem;
            height: 1rem;
            border-radius: 50%;
            background-color: var(--primary);
        }
        
        .timeline-item:after {
            content: '';
            position: absolute;
            left: 0.5rem;
            top: 1.25rem;
            width: 0.125rem;
            height: calc(100% + 1rem);
            background-color: var(--light-gray);
        }
        
        .timeline-item:last-child:after {
            display: none;
        }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    """)

# Create navigation component
def create_navigation():
    with ui.header().classes('flex justify-between items-center p-4 bg-white shadow-sm'):
        ui.label(settings.APP_NAME).classes('text-xl font-bold text-gray-800')
        
        with ui.row().classes('gap-2'):
            ui.button('Home', on_click=lambda: ui.navigate.to('/')).props('flat').classes('nav-link')
            ui.button('Projects', on_click=lambda: ui.navigate.to('/#projects')).props('flat').classes('nav-link')
            ui.button('Skills', on_click=lambda: ui.navigate.to('/#skills')).props('flat').classes('nav-link')
            ui.button('Experience', on_click=lambda: ui.navigate.to('/#experience')).props('flat').classes('nav-link')
            ui.button('Contact', on_click=lambda: ui.navigate.to('/#contact')).props('flat').classes('nav-link')

# Create footer component
def create_footer():
    with ui.footer().classes('p-6 bg-gray-800 text-white'):
        with ui.column().classes('w-full max-w-6xl mx-auto'):
            with ui.row().classes('justify-between items-center flex-wrap'):
                ui.label(f'© {settings.OWNER_NAME} {2024}').classes('text-gray-400')
                
                with ui.row().classes('gap-4'):
                    if settings.OWNER_GITHUB:
                        ui.link(target=settings.OWNER_GITHUB, new_tab=True).classes('social-icon').style('color: white;').html('<i class="fab fa-github"></i>')
                    if settings.OWNER_LINKEDIN:
                        ui.link(target=settings.OWNER_LINKEDIN, new_tab=True).classes('social-icon').style('color: white;').html('<i class="fab fa-linkedin"></i>')
                    if settings.OWNER_TWITTER:
                        ui.link(target=settings.OWNER_TWITTER, new_tab=True).classes('social-icon').style('color: white;').html('<i class="fab fa-twitter"></i>')
                    if settings.OWNER_EMAIL:
                        ui.link(f'mailto:{settings.OWNER_EMAIL}', new_tab=True).classes('social-icon').style('color: white;').html('<i class="fas fa-envelope"></i>')

# Define page routes
@ui.page('/')
def home_page():
    """Main portfolio page."""
    create_navigation()
    
    # Hero Section
    with ui.column().classes('w-full hero-section'):
        with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-16'):
            with ui.row().classes('items-center flex-wrap'):
                # Profile information
                with ui.column().classes('w-full md:w-2/3 mb-8 md:mb-0'):
                    ui.label(f"Hello, I'm {settings.OWNER_NAME}").classes('text-4xl font-bold mb-2')
                    ui.label(settings.OWNER_TITLE).classes('text-2xl mb-6')
                    ui.markdown(portfolio_service.get_bio()).classes('text-lg opacity-90')
                    
                    with ui.row().classes('mt-6 gap-4'):
                        ui.button('View Projects', on_click=lambda: ui.navigate.to('/#projects')).props('unelevated').classes('bg-white text-indigo-600 font-medium')
                        ui.button('Contact Me', on_click=lambda: ui.navigate.to('/#contact')).props('outline').classes('text-white border-white')
                
                # Profile image
                with ui.column().classes('w-full md:w-1/3 flex justify-center'):
                    profile_path = f"/static/{settings.OWNER_PROFILE_IMAGE}"
                    ui.image(profile_path).classes('rounded-full w-64 h-64 object-cover border-4 border-white shadow-lg')
    
    # Main content
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # About Section
        with ui.column().classes('section') as about_section:
            about_section.props('id=about')
            ui.label('About Me').classes('text-3xl font-bold mb-6')
            ui.markdown(portfolio_service.get_about()).classes('text-lg')
        
        # Skills Section
        with ui.column().classes('section') as skills_section:
            skills_section.props('id=skills')
            ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6')
            
            # Technical Skills
            ui.label('Technical Skills').classes('text-xl font-semibold mb-4')
            with ui.row().classes('flex-wrap gap-2 mb-6'):
                for skill in portfolio_service.get_technical_skills():
                    ui.label(skill).classes('skill-tag')
            
            # AI & ML Skills
            ui.label('AI & Machine Learning').classes('text-xl font-semibold mb-4')
            with ui.row().classes('flex-wrap gap-2 mb-6'):
                for skill in portfolio_service.get_ai_ml_skills():
                    ui.label(skill).classes('skill-tag')
            
            # Tools & Platforms
            ui.label('Tools & Platforms').classes('text-xl font-semibold mb-4')
            with ui.row().classes('flex-wrap gap-2'):
                for skill in portfolio_service.get_tools_platforms():
                    ui.label(skill).classes('skill-tag')
        
        # Projects Section
        with ui.column().classes('section') as projects_section:
            projects_section.props('id=projects')
            ui.label('Featured Projects').classes('text-3xl font-bold mb-6')
            
            with ui.grid(columns=3).classes('gap-6'):
                for project in portfolio_service.get_projects():
                    with ui.card().classes('card h-full'):
                        if project.get('image'):
                            ui.image(f"/static/{project['image']}").classes('w-full h-48 object-cover')
                        
                        with ui.card_section():
                            ui.label(project['title']).classes('text-xl font-bold')
                            ui.label(project['category']).classes('text-sm text-gray-500 mb-2')
                            ui.markdown(project['description']).classes('text-sm mb-4')
                            
                            with ui.row().classes('flex-wrap gap-1 mb-4'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('text-xs skill-tag py-1 px-2')
                            
                            with ui.row().classes('gap-2'):
                                if project.get('demo_url'):
                                    ui.link('Live Demo', project['demo_url'], new_tab=True).classes('text-sm text-primary font-medium')
                                if project.get('github_url'):
                                    ui.link('GitHub', project['github_url'], new_tab=True).classes('text-sm text-primary font-medium')
        
        # Experience Section
        with ui.column().classes('section') as experience_section:
            experience_section.props('id=experience')
            ui.label('Work Experience').classes('text-3xl font-bold mb-6')
            
            for job in portfolio_service.get_experience():
                with ui.column().classes('timeline-item'):
                    with ui.row().classes('justify-between items-start mb-1'):
                        ui.label(job['title']).classes('text-xl font-bold')
                        ui.label(f"{job['start_date']} - {job['end_date']}").classes('text-sm text-gray-500')
                    ui.label(job['company']).classes('text-lg font-medium text-primary mb-2')
                    ui.markdown(job['description']).classes('mb-2')
                    
                    with ui.row().classes('flex-wrap gap-1 mb-2'):
                        for tech in job['technologies']:
                            ui.label(tech).classes('text-xs skill-tag py-1 px-2')
        
        # Education Section
        with ui.column().classes('section') as education_section:
            education_section.props('id=education')
            ui.label('Education').classes('text-3xl font-bold mb-6')
            
            for edu in portfolio_service.get_education():
                with ui.column().classes('timeline-item'):
                    with ui.row().classes('justify-between items-start mb-1'):
                        ui.label(edu['degree']).classes('text-xl font-bold')
                        ui.label(f"{edu['start_date']} - {edu['end_date']}").classes('text-sm text-gray-500')
                    ui.label(edu['institution']).classes('text-lg font-medium text-primary mb-2')
                    ui.markdown(edu['description']).classes('mb-2')
        
        # Contact Section
        with ui.column().classes('section') as contact_section:
            contact_section.props('id=contact')
            ui.label('Get In Touch').classes('text-3xl font-bold mb-6')
            
            with ui.row().classes('flex-wrap'):
                # Contact form
                with ui.column().classes('w-full lg:w-1/2 pr-0 lg:pr-8 mb-8 lg:mb-0'):
                    ui.label('Send me a message').classes('text-xl font-semibold mb-4')
                    
                    name_input = ui.input('Your Name').classes('w-full mb-4')
                    email_input = ui.input('Your Email').classes('w-full mb-4').props('type=email')
                    subject_input = ui.input('Subject').classes('w-full mb-4')
                    message_input = ui.textarea('Message').classes('w-full mb-4').props('rows=5')
                    
                    async def handle_contact_form():
                        # In a real app, this would send an email or store the message
                        if not name_input.value or not email_input.value or not message_input.value:
                            ui.notify('Please fill out all required fields', type='negative')
                            return
                        
                        ui.notify('Message sent successfully! I will get back to you soon.', type='positive')
                        name_input.value = ''
                        email_input.value = ''
                        subject_input.value = ''
                        message_input.value = ''
                    
                    ui.button('Send Message', on_click=handle_contact_form).props('unelevated').classes('bg-primary text-white')
                
                # Contact information
                with ui.column().classes('w-full lg:w-1/2'):
                    ui.label('Contact Information').classes('text-xl font-semibold mb-4')
                    
                    with ui.column().classes('space-y-4'):
                        with ui.row().classes('items-center'):
                            ui.icon('email').classes('text-primary mr-2')
                            ui.link(f'mailto:{settings.OWNER_EMAIL}', settings.OWNER_EMAIL).classes('text-primary')
                        
                        if settings.OWNER_GITHUB:
                            with ui.row().classes('items-center'):
                                ui.icon('code').classes('text-primary mr-2')
                                ui.link(settings.OWNER_GITHUB, 'GitHub', new_tab=True).classes('text-primary')
                        
                        if settings.OWNER_LINKEDIN:
                            with ui.row().classes('items-center'):
                                ui.icon('work').classes('text-primary mr-2')
                                ui.link(settings.OWNER_LINKEDIN, 'LinkedIn', new_tab=True).classes('text-primary')
                        
                        if settings.OWNER_TWITTER:
                            with ui.row().classes('items-center'):
                                ui.icon('chat').classes('text-primary mr-2')
                                ui.link(settings.OWNER_TWITTER, 'Twitter', new_tab=True).classes('text-primary')
    
    create_footer()

# Create the portfolio service:
<HST-write file_path="app/services/portfolio_service.py">
"""
Portfolio Service - Manages portfolio data and content
"""
from typing import List, Dict, Any, Optional
import logging
import os
from app.core.config import settings

logger = logging.getLogger(__name__)

class PortfolioService:
    """Service for managing portfolio content."""
    
    def __init__(self):
        """Initialize the portfolio service with default data."""
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize portfolio data."""
        # Bio - short introduction
        self._bio = """
        I'm a passionate AI Engineer with expertise in machine learning, deep learning, 
        and natural language processing. I build intelligent systems that solve real-world problems.
        """
        
        # About - longer description
        self._about = """
        As an AI Engineer with over 5 years of experience, I specialize in developing cutting-edge 
        artificial intelligence solutions that drive business value. My expertise spans machine learning, 
        deep learning, natural language processing, and computer vision.

        I'm passionate about creating AI systems that are not only technically sound but also 
        ethical, explainable, and user-friendly. My approach combines strong theoretical knowledge 
        with practical implementation skills to deliver solutions that make a real impact.

        Throughout my career, I've worked on diverse projects ranging from recommendation systems 
        and predictive analytics to conversational AI and image recognition. I enjoy tackling 
        complex problems and transforming raw data into actionable insights and intelligent applications.
        """
        
        # Technical skills
        self._technical_skills = [
            "Python", "TensorFlow", "PyTorch", "Scikit-learn", "Keras", 
            "SQL", "NoSQL", "Docker", "Kubernetes", "Git", 
            "REST APIs", "FastAPI", "Flask", "Django", "AWS"
        ]
        
        # AI & ML skills
        self._ai_ml_skills = [
            "Machine Learning", "Deep Learning", "Natural Language Processing", 
            "Computer Vision", "Reinforcement Learning", "Neural Networks", 
            "Generative AI", "LLMs", "Transformers", "BERT", "GPT", 
            "Data Mining", "Feature Engineering", "Model Deployment"
        ]
        
        # Tools & platforms
        self._tools_platforms = [
            "AWS SageMaker", "Google Cloud AI", "Azure ML", "Hugging Face", 
            "MLflow", "Weights & Biases", "Jupyter", "Pandas", "NumPy", 
            "Matplotlib", "Streamlit", "Gradio", "CUDA", "Ray"
        ]
        
        # Projects
        self._projects = [
            {
                "title": "Intelligent Document Processing System",
                "category": "Natural Language Processing",
                "description": "Developed an end-to-end document processing system using transformer-based models to extract, classify, and analyze information from unstructured documents.",
                "technologies": ["PyTorch", "Transformers", "FastAPI", "Docker", "AWS"],
                "image": "project1.jpg",
                "github_url": "https://github.com/yourusername/document-processing",
                "demo_url": "https://demo-url.com/document-processing"
            },
            {
                "title": "Predictive Maintenance AI",
                "category": "Time Series Analysis",
                "description": "Built a predictive maintenance system for industrial equipment using time series forecasting and anomaly detection algorithms.",
                "technologies": ["TensorFlow", "Keras", "Prophet", "Docker", "Azure"],
                "image": "project2.jpg",
                "github_url": "https://github.com/yourusername/predictive-maintenance"
            },
            {
                "title": "Conversational AI Assistant",
                "category": "Natural Language Processing",
                "description": "Created a domain-specific conversational AI assistant using fine-tuned LLMs and retrieval-augmented generation techniques.",
                "technologies": ["PyTorch", "Hugging Face", "LangChain", "FastAPI", "Redis"],
                "image": "project3.jpg",
                "github_url": "https://github.com/yourusername/conversational-ai",
                "demo_url": "https://demo-url.com/assistant"
            },
            {
                "title": "Computer Vision for Retail Analytics",
                "category": "Computer Vision",
                "description": "Implemented a computer vision system for retail stores to analyze customer behavior, optimize store layouts, and improve the shopping experience.",
                "technologies": ["PyTorch", "OpenCV", "YOLO", "TensorRT", "Kubernetes"],
                "image": "project4.jpg",
                "github_url": "https://github.com/yourusername/retail-vision"
            },
            {
                "title": "Recommendation Engine",
                "category": "Recommender Systems",
                "description": "Designed and deployed a hybrid recommendation engine combining collaborative filtering and content-based approaches for a media streaming platform.",
                "technologies": ["TensorFlow", "Scikit-learn", "FastAPI", "PostgreSQL", "AWS"],
                "image": "project5.jpg",
                "github_url": "https://github.com/yourusername/recommendation-engine"
            },
            {
                "title": "AI Model Monitoring Platform",
                "category": "MLOps",
                "description": "Built a comprehensive platform for monitoring ML models in production, detecting drift, and automating retraining processes.",
                "technologies": ["Python", "Prometheus", "Grafana", "Docker", "Kubernetes"],
                "image": "project6.jpg",
                "github_url": "https://github.com/yourusername/model-monitoring"
            }
        ]
        
        # Experience
        self._experience = [
            {
                "title": "Senior AI Engineer",
                "company": "TechCorp AI",
                "start_date": "Jan 2022",
                "end_date": "Present",
                "description": """
                * Led the development of a large-scale NLP system for document processing, improving accuracy by 35%
                * Designed and implemented a computer vision solution for manufacturing quality control
                * Mentored junior engineers and established best practices for ML model development and deployment
                * Collaborated with product teams to define AI roadmap and technical requirements
                """,
                "technologies": ["PyTorch", "Transformers", "FastAPI", "Docker", "Kubernetes", "AWS"]
            },
            {
                "title": "Machine Learning Engineer",
                "company": "DataSmart Solutions",
                "start_date": "Mar 2019",
                "end_date": "Dec 2021",
                "description": """
                * Developed recommendation algorithms that increased user engagement by 28%
                * Built and deployed predictive models for customer churn reduction
                * Implemented data pipelines for efficient processing of large datasets
                * Collaborated with data scientists to optimize model performance
                """,
                "technologies": ["TensorFlow", "Scikit-learn", "Keras", "SQL", "Airflow", "GCP"]
            },
            {
                "title": "Data Scientist",
                "company": "AI Innovations",
                "start_date": "Jun 2017",
                "end_date": "Feb 2019",
                "description": """
                * Conducted exploratory data analysis and feature engineering for various ML projects
                * Developed classification models for customer segmentation
                * Created interactive dashboards for visualizing model results
                * Participated in client meetings to present findings and recommendations
                """,
                "technologies": ["Python", "Pandas", "Scikit-learn", "Matplotlib", "SQL", "Tableau"]
            }
        ]
        
        # Education
        self._education = [
            {
                "degree": "Master of Science in Artificial Intelligence",
                "institution": "Stanford University",
                "start_date": "2015",
                "end_date": "2017",
                "description": """
                * Specialized in Machine Learning and Natural Language Processing
                * Research assistant in the AI Lab working on deep learning applications
                * Thesis: "Attention Mechanisms in Neural Networks for Document Classification"
                """
            },
            {
                "degree": "Bachelor of Science in Computer Science",
                "institution": "University of California, Berkeley",
                "start_date": "2011",
                "end_date": "2015",
                "description": """
                * Minor in Mathematics
                * Dean's List for Academic Excellence
                * Participated in AI and Machine Learning student research group
                """
            }
        ]
    
    def get_bio(self) -> str:
        """Get the short bio."""
        return self._bio
    
    def get_about(self) -> str:
        """Get the about section content."""
        return self._about
    
    def get_technical_skills(self) -> List[str]:
        """Get technical skills list."""
        return self._technical_skills
    
    def get_ai_ml_skills(self) -> List[str]:
        """Get AI and ML specific skills."""
        return self._ai_ml_skills
    
    def get_tools_platforms(self) -> List[str]:
        """Get tools and platforms list."""
        return self._tools_platforms
    
    def get_projects(self) -> List[Dict[str, Any]]:
        """Get projects list."""
        return self._projects
    
    def get_experience(self) -> List[Dict[str, Any]]:
        """Get work experience list."""
        return self._experience
    
    def get_education(self) -> List[Dict[str, Any]]:
        """Get education list."""
        return self._education
    
    def update_bio(self, new_bio: str) -> None:
        """Update the bio."""
        self._bio = new_bio
    
    def update_about(self, new_about: str) -> None:
        """Update the about section."""
        self._about = new_about
    
    def add_project(self, project: Dict[str, Any]) -> None:
        """Add a new project."""
        self._projects.append(project)
    
    def add_experience(self, experience: Dict[str, Any]) -> None:
        """Add a new work experience."""
        self._experience.append(experience)
    
    def add_education(self, education: Dict[str, Any]) -> None:
        """Add a new education entry."""
        self._education.append(education)