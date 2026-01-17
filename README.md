# Comparative Genomics Analysis Web Application
This project is a local web application developed for the rapid and comparative analysis of biological data. It performs automated queries on the NCBI (National Center for Biotechnology Information) database using a user-defined list of organisms and Gene Ontology (GO) or Enzyme Commission (EC) numbers. The results are presented in an easy-to-understand comparative matrix (table).

# Installation
Before running the project, you need to install the required Python libraries.

Install dependencies: Open your terminal or command prompt in the project directory and run the following command:

pip install -r requirements.txt
This command will install the Flask and BioPython libraries required for the project.

# How to Run
Once the dependencies are installed, run the following command in the terminal to start the application:

python app.py
When the application starts, you will see an output similar to the following:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
This indicates that the web server is running on port 5000 of your local machine.

# How to Use
Open your web browser and navigate to http://127.0.0.1:5000/.

In the "Organisms" box, enter the scientific names of the organisms you wish to analyze, one per line.

In the "GO or EC Numbers" box, enter the Gene Ontology or Enzyme Commission numbers you wish to search for, one per line.

Click the "Start Analysis" button.

The application will query the NCBI database for each organism and term pair and present the results in a matrix table. A ✓ mark in the table indicates that a record corresponding to that term was found in the respective organism.
