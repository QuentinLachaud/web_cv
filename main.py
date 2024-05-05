import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Define functions for each section
def display_cv():
    st.markdown('# Quentin Lachaud')
    st.write('''Welcome to my online CV!
             I made this because LinkedIn is a bit boring and I wanted to show off some skills and projects...''')

    st.divider()

    about_me_col, tech_stack_col = st.columns([1, 1])

    with about_me_col:

        about_me = st.expander(label=':eyes: About me', expanded=True)
        with about_me:
            st.markdown('''
                        - **:green[3 years]** experience in the financial sector
                        - **:green[6 years]** hands-on Python
                        - **:green[10 years]** Data Analysis & Statistics
                        ''')
    with tech_stack_col:
        tech_stack = st.expander(label=':wrench: Tech Stack', expanded=True)
        with tech_stack:
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.markdown('''
                            - Python
                            - SQL
                            - AWS
                            - SageMaker Studio
                            - Git/GitLab/GitHub
                            ''')
            with col2:
                st.markdown('''
                            - matplotlib/seaborn
                            - Athena/s3
                            - statsmodels
                            - pandas
                            - numpy
                            ''')
            with col3:
                st.markdown('''
                            - scikit-learn
                            - BeautifulSoup
                            - Selenium
                            ''')
            
    st.divider()
    

    job_col, edu_col = st.columns([1, 1])

    with job_col:

        professional_experience = st.expander(label=':briefcase: Professional Experience', expanded=True)
        with professional_experience:

            
        

            st.markdown('''
                        ##### :red[Data Scientist] - NatWest Group, Edinburgh UK *:grey[(Hybrid)]*
                        :blue[*(Mar 2023 - Present)*]\n

                        - Automated profitability reporting, reducing human error and hours of excel work.
                        - Data pipeline ingestion, wrangling, and cleaning.
                        - Implemented regression-based predictive model in loans behavior.
                        - Documentation and repository implementation for team codebase.''')

            st.markdown('''            
                        --------------
                                    
                        ##### :red[Junior Data Scientist] - Strike, Colchester, UK *:grey[(Remote)]*
                        :blue[*(Mar 2021 - Feb 2023)*]\n

                        - Financial reconciliation + machine learning forecasts using Python
                        - Data wrangling + cleaning/normalisation
                        - Produced cohort-based data transformation pipelines for forecasting
                        - Produced data visualisations (matplotlib, seaborn, plotly)
                        - A/B testing business propositions using SciPy
                        - Statistical power calculation''')

            st.markdown('''
                        ----------------
                        
                        ##### :red[Postdoctoral Researcher] - University of Glasgow, UK
                        :blue[*(Oct 2018 - Jul 2021)*]\n

                        - 1st author Cardiovascular Research (2021) impact factor: 8.1
                        - Published in Circulation Research (2017) impact factor: 17.3
                        - Trained PhD candidates in data techniques ( statistics, visualisation and presentation )
                        - Implemented data cleaning pipelines in Python
                        - Produced publication-grade data visualisations and statistical analyses
                        - Created and optimised hypothesis-driven experimental protocols
                                    
                        
                        ''')

    with edu_col:
        education = st.expander(label=':books: Education', expanded=True)
        with education:
            st.markdown('''
                        ##### :red[Ph.D. Electrophysiology] - University of Glasgow, UK
                        :blue[*(Sep 2015 - Aug 2019)*]\n

                        - Automated profitability reporting, reducing human error and hours of excel work.
                        - Data pipeline ingestion, wrangling, and cleaning.
                        - Implemented regression-based predictive model in loans behavior.
                        - Documentation and repository implementation for team codebase.''')
            
            st.markdown('''
                        ##### :red[M.Sc. (Research) Transaltional Medicine] - University of Glasgow, UK
                        :blue[*(Sep 2014 - Aug 2015)*]\n

                        - Automated profitability reporting, reducing human error and hours of excel work.
                        - Data pipeline ingestion, wrangling, and cleaning.
                        - Implemented regression-based predictive model in loans behavior.
                        - Documentation and repository implementation for team codebase.''')
            
            st.markdown('''
                        ##### :red[B.Sc. Neuroscience] - University of Glasgow, UK
                        :blue[*(Sep 2009 - May 2013)*]\n

                        - Automated profitability reporting, reducing human error and hours of excel work.
                        - Data pipeline ingestion, wrangling, and cleaning.
                        - Implemented regression-based predictive model in loans behavior.
                        - Documentation and repository implementation for team codebase.''')

def display_projects():
    st.title('Projects')
    st.divider()

    project_col1, project_col2 = st.columns([1, 1])
    with project_col1:
        finance_app_expander = st.expander('Personal Finance Web App', expanded=True)
        with finance_app_expander:
         
            st.markdown('''
                        ### :money_with_wings: :blue[Personal Finance Web App]
                        - **Description:** [Web app](https://personal-finance-app.streamlit.app/) to extrapolate your personal finance data
                        - **Tech Stack:** :rainbow[Python], Streamlit, Plotly, Pandas, Numpy
                        ''')
            st.divider()
            st.markdown('### :camera: Screenshots')

            st.write(':grey[Insert your assets and liabilities, estimate a growth rate and project the future!]')
            st.image('images/finance_app_net_worth_page.png', use_column_width=True)

            st.divider()
            st.write(':grey[Simulate 1000 investment/retirement outcomes based on your inputs]')
            st.image('images/monte_carlo_simulation_page.png', use_column_width=True)

            st.divider()
            st.write(':grey[Calculate mortgage payments and overpayment effects]')
            st.image('images/mortgage_calculator_page.png', use_column_width=True)
            

# Mapping of section names to corresponding functions
section_functions = {
    'CV': display_cv,
    'Projects': display_projects,
}

# Sidebar setup
with st.sidebar:
    
    st.image('images/white.png', width=230)
    st.divider()
    nav_expander = st.expander('Sections', expanded=True)

    with nav_expander:

        selection = st.radio(label='  ', options=(list(section_functions.keys())))            

    st.divider()

    st.write('### Contact')
    github_logo_url   = 'https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png'
    linkedin_logo_url = 'https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-1024.png'
    st.write(':email: quentin.lachaud@gmail.com')
    st.write(':telephone_receiver: :blue[(+44) 7513 471 478]')
    st.write('\n'*5)
    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown(f'<a href="https://www.linkedin.com/in/quentinlachaud" target="_blank"><img src="{linkedin_logo_url}" alt="LinkedIn Logo" width="40"></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://github.com/QuentinLachaud" target="_blank"><img src="{github_logo_url}" alt="GitHub Logo" width="40"></a>', unsafe_allow_html=True)




# Display the selected section
selected_function = section_functions.get(selection)
if selected_function:
    selected_function()

