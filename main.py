import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Define functions for each section
def display_resume():
    st.title('Resume')
    about_me_col, tech_stack_col = st.columns([1, 1])
    with about_me_col:
        about_me = st.expander(label=':eyes: About me', expanded=True)
        with about_me:
            st.markdown('''
                        - Research scientist turned data scientist in 2021
                        - 3 years experience in the financial sector
                        - 6 years hands-on Python
                        - 10 years data analytics & Statistics
                        ''')
    with tech_stack_col:
        tech_stack = st.expander(label=':wrench: Tech Stack', expanded=True)
        with tech_stack:
            col1, col2, col3 = st.columns([1.5, 1.5, 1])
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
    professional_experience = st.expander(label=':purple[Professional Experience]', expanded=True)
    education               = st.expander(label=':books: Education', expanded=True)

    with professional_experience:

            
        

        st.markdown('''
        ##### Data Scientist - NatWest Group, Edinburgh UK *(Hybrid)*
        :green[*(Mar 2023 - Present)*]\n

        - Automated profitability reporting, reducing human error and hours of excel work.
        - Data pipeline ingestion, wrangling, and cleaning.
        - Implemented regression-based predictive model in loans behavior.
        - Documentation and repository implementation for team codebase.''')

        st.markdown('''            
        --------------
                    
        ##### Junior Data Scientist - Strike, Colchester *(Remote)*
        :green[*(Mar 2021 - Feb 2023)*]\n

        - Financial reconciliation + machine learning forecasts using Python
        - Data wrangling + cleaning/normalisation
        - Produced cohort-based data transformation pipelines for forecasting
        - Produced data visualisations (matplotlib, seaborn, plotly)
        - A/B testing business propositions using SciPy
        - Statistical power calculation''')

        st.markdown('''
        ----------------
                    
        ##### Postdoctoral Researcher - University of Glasgow, Glasgow UK
        :green[*(Oct 2018 - Jul 2021)*]\n

        - 1st author Cardiovascular Research (2021) impact factor: 8.1
        - Published in Circulation Research (2017) impact factor: 17.3
        - Trained PhD candidates in data techniques ( statistics, visualisation and presentation )
        - Implemented data cleaning pipelines in Python
        - Produced publication-grade data visualisations and statistical analyses
        - Created and optimised hypothesis-driven experimental protocols
                    
        
        '''
        )

    with education:
        st.write('University of Glasgow 4 lyf')

def display_projects():
    st.title('Projects')
    st.write('These are my projects')

def display_contact():
    st.title('Contact')
    st.write('This is how you can contact me')


# Mapping of section names to corresponding functions
section_functions = {
    'Resume': display_resume,
    'Projects': display_projects,
    'Contact': display_contact
}

# Sidebar setup
with st.sidebar:

    st.title('Quentin Lachaud')
    st.divider()
    col1, col2, col3 =  st.columns([.3, 2, .1])
    with col2:
        st.caption(':arrow_down: Navigate through the sections below :arrow_down:')
    selection = st.radio(label='', options=(list(section_functions.keys())))

# Display the selected section
selected_function = section_functions.get(selection)
if selected_function:
    selected_function()

