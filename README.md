
![YoutubeSafetyIndex](https://github.com/user-attachments/assets/9396c3e4-c4e2-407b-9d71-1bff7e4321b9)

# YouTube Safety Index: A Retrieval and Classification System

## Overview

The **YouTube Safety Index** is a content monitoring system designed to help parents/guardians track and analyze the YouTube content consumed by children. By leveraging **Information Retrieval (IR)** methodologies and **Machine Learning (ML)** models, the system captures, categorizes, and evaluates videos based on safety metrics, providing real-time alerts for potentially unsafe content.

## Features

- **YouTube Traffic Capture:** Monitors household Wi-Fi traffic and captures YouTube video data.
- **Content Indexing:** Indexes YouTube video logs into **ElasticSearch** for efficient storage, filtering, and retrieval.
- **Content Categorization:** Classifies videos as safe or unsafe using a **BERT-based ML model**.
- **Real-time Alerts:** Sends notifications via **SMTP email** and **Kibana** alerts for flagged unsafe content.
- **Actionable Insights:** Provides a user-friendly interface for viewing the safety status of videos.

## Installation

1. **Clone the Repository:**
   

2. **Install Dependencies:**
   Install the necessary Python packages:

3. **Setup ElasticSearch & Kibana:**
   - Install and configure **ElasticSearch** for indexing YouTube logs.
   - Set up **Kibana** to visualize logs and create alert rules.

4. **Configure YouTube API:**
   - Create a project on **Google Cloud Console** and enable the **YouTube Data API v3**.
   - Retrieve the API key and set it in your environment variables:
     ```bash
     export YOUTUBE_API_KEY="your_api_key"
     ```

5. **Run the Traffic Capture:**
   Use **Postman Proxy** with SSL bumping to capture YouTube traffic on your local network.

## Components

### 1. **Traffic Capture (Postman Proxy)**
   - Intercepts household Wi-Fi traffic and captures YouTube URLs, video IDs, and metadata.

### 2. **ElasticSearch Indexing**
   - Processes and stores the captured YouTube logs (video IDs, URLs, timestamps) into **ElasticSearch** for easy retrieval.

### 3. **Metadata & Transcript Retrieval**
   - Uses the **YouTube Data API v3** to fetch video metadata and captions for content analysis.

### 4. **Content Categorization**
   - A **BERT-based model** is used to classify videos as safe or unsafe based on their metadata and transcripts.
   - Utilizes predefined lexicons for profanity, violence, and abuse filtering.

### 5. **Real-Time Alerts**
   - **Kibana** alerts notify users of flagged unsafe content.
   - **SMTP email alerts** are sent to users when an unsafe video is detected.

## Model Evaluation

The **BERT-based classification model** is evaluated using the following metrics:

- **Precision:**
  - Unsafe Videos (Class 0): 0.86
  - Safe Videos (Class 1): 0.77

- **Recall:**
  - Unsafe Videos (Class 0): 0.90
  - Safe Videos (Class 1): 0.69

- **F1-Score:**
  - Unsafe Videos (Class 0): 0.88
  - Safe Videos (Class 1): 0.73

- **Weighted Average F1-Score:** 0.83  
- **Accuracy:** 83%

## Technologies Used

- **Python**: Core programming language for scripts and model development.
- **BERT**: Pretrained model for text classification (used for categorizing content).
- **YouTube Data API v3**: Fetches video metadata and captions.
- **ElasticSearch**: Indexes video logs for fast retrieval and filtering.
- **Kibana**: Visualizes data, provides querying, and sets up real-time alerts.
- **Postman Proxy**: Captures YouTube HTTPS traffic with SSL bumping.
- **SMTP**: Sends email alerts when unsafe content is flagged.

## How It Works

1. **Traffic Capture:** The system captures YouTube traffic from the household network.
2. **Data Indexing:** Captured data (video IDs, URLs) is processed and indexed into **ElasticSearch**.
3. **Metadata Retrieval:** Video metadata and transcripts are retrieved using the **YouTube API**.
4. **Content Classification:** The **BERT model** classifies videos as **safe** or **unsafe** based on metadata and transcripts.
5. **Alerts:** Real-time alerts notify users via **Kibana** and **SMTP email** when unsafe content is identified.

## Use Cases

- **Parents/Guardians:** Monitor the safety of videos consumed by children and receive real-time alerts for inappropriate content.
- **Researchers/Developers:** Use the system as a basis for developing and testing video content safety algorithms.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **ElasticSearch** and **Kibana** for data indexing and visualization.
- **BERT** for text classification tasks.
- **YouTube API** for metadata retrieval.
