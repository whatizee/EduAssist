
```markdown
# EduAssist

EduAssist is an AI-powered chatbot designed for St. Clair College students and prospective applicants. It uses the Mistral 7B model to answer common questions about courses, locations, syllabus details, and more. This interactive chatbot provides accurate and quick responses to improve the user experience.

---

## Features

- **AI-Powered Chat**: Utilizes the Mistral 7B model for intelligent responses.
- **Custom FAQ Integration**: Answers pre-defined common questions from a dataset.
- **User-Friendly Interface**: Simple web-based UI for real-time interaction.
- **Dynamic Responses**: Handles queries outside the FAQ dataset using the AI model.
- **Extensible Design**: Easily customizable for additional features or datasets.

---



## Getting Started

Follow these steps to set up EduAssist on your local machine:

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/whatizee/EduAssist.git
   cd EduAssist
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:
   - Place your FAQ dataset (`faq.csv`) in the `dataset/` folder.

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## Project Structure

```
EduAssist/
├── app.py              # Main Flask backend
├── templates/
│   └── index.html      # Chatbot frontend
├── static/
│   ├── style.css       # CSS styling
│   └── script.js       # JavaScript logic
├── dataset/
│   └── faq.csv         # FAQ dataset
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── .env                # Optional: Environment variables
```

---

## Dataset

The chatbot relies on an FAQ dataset (`dataset/faq.csv`) structured as follows:

| question                                 | answer                                                                 |
|------------------------------------------|------------------------------------------------------------------------|
| What are the courses available for IT?   | Courses include Data Analytics, Cloud Computing, and IT Networking.   |
| Where is the college located?            | St. Clair College is in Windsor, Ontario, Canada.                     |
| Does the syllabus include deep learning? | Yes, some courses include deep learning modules.                      |

You can extend this dataset to include more FAQs.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **AI Model**: Mistral 7B
- **Data Handling**: Pandas
- **Deployment**: Local/Cloud (e.g., Azure)

---

## Contributing

Contributions are welcome! If you’d like to add features or fix bugs:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them to your branch:
   ```bash
   git commit -m "Add feature"
   git push origin feature-name
   ```
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, feel free to reach out:

- **Author**: [Your Name](https://github.com/whatizee)
- **Email**: [jibinjks@gmail.com](mailto:jibinjks@gmail.com)

---

## Acknowledgments

Special thanks to St. Clair College for inspiring this project and Mistral AI for the powerful open-source model.

``` 

Feel free to customize the content based on your needs or update the placeholder links with actual resources. Let me know if you'd like any additional sections or edits!
