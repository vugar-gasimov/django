from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challanges = {
    "january": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "february": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "march": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "april": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "may": "Task: Create new features from existing data to improve the performance of machine learning models. Use libraries like scikit-learn for feature extraction and transformation techniques. Example: Engineer new features from text data (e.g., sentiment analysis) to improve sentiment classification models.",
    "june": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "july": "Task: Evaluate the performance of your trained model using metrics like accuracy, precision, recall, and F1 score. Consider techniques like cross-validation for robust evaluation. Example: Evaluate the performance of a spam classification model and tune its hyperparameters for optimal results.",
    "august": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "september": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "october": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "november": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
    "december": "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.",
}

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("This month is not supported.")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
        
    return HttpResponseRedirect(redirect_path)
# def monthly_challange_by_number(request, month):
#     challange_text = None
#     if month == 1:
#         challange_text = "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies."
#     elif month == 2:
#         challange_text = "Task: Build a Python script to automate data extraction from various sources (APIs, databases, web scraping) and implement data cleaning routines using libraries like pandas. Example: Develop a script to automatically download weather data from an API and clean it for inconsistencies or missing values."
#     elif month == 3:
#         challange_text = "Task: Evaluate the performance of your trained model using metrics like accuracy, precision, recall, and F1 score. Consider techniques like cross-validation for robust evaluation. Example: Evaluate the performance of a spam classification model and tune its hyperparameters for optimal results."
#     else:
#         return HttpResponseNotFound("This month is not supported.")
#     return HttpResponse(challange_text)
    
def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        return HttpResponse(challange_text)
    except:
        return HttpResponseNotFound("This month is not supported.")
# def monthly_challange(request, month):
#     challange_text = None
#     if month == "january":
#         challange_text = "Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies."
#     elif month == "february":
#         challange_text = "Task: Build a Python script to automate data extraction from various sources (APIs, databases, web scraping) and implement data cleaning routines using libraries like pandas. Example: Develop a script to automatically download weather data from an API and clean it for inconsistencies or missing values."
#     elif month == "march":
#         challange_text = "Task: Evaluate the performance of your trained model using metrics like accuracy, precision, recall, and F1 score. Consider techniques like cross-validation for robust evaluation. Example: Evaluate the performance of a spam classification model and tune its hyperparameters for optimal results."
#     else:
#         return HttpResponseNotFound("This month is not supported.")
#     return HttpResponse(challange_text)

# def january(request):
#     return HttpResponse("Task: Analyze historical data to identify trends and seasonality in your chosen domain. Use libraries like pandas and matplotlib to visualize patterns and set data-driven goals for the year. Example: Analyze sales data for the past year to predict peak sales periods and inform inventory management strategies.")


# def february(request):
#     return HttpResponse("Task: Build a Python script to automate data extraction from various sources (APIs, databases, web scraping) and implement data cleaning routines using libraries like pandas. Example: Develop a script to automatically download weather data from an API and clean it for inconsistencies or missing values.")


# def april(request):
#     return HttpResponse("Task: Perform exploratory data analysis (EDA) on a new dataset to understand its characteristics, identify potential relationships, and uncover interesting insights. Use libraries like pandas, NumPy, and seaborn for data manipulation and visualization. Example: Explore a customer dataset to identify customer segments with different purchase behavior.")

# def may(request):
#     return HttpResponse("Task: Create new features from existing data to improve the performance of machine learning models. Use libraries like scikit-learn for feature extraction and transformation techniques. Example: Engineer new features from text data (e.g., sentiment analysis) to improve sentiment classification models.")

# def june(request):
#     return HttpResponse("Task: Train a machine learning model for a specific task (regression, classification, clustering). Use libraries like scikit-learn, TensorFlow, or PyTorch for model building and training. Example: Train a regression model to predict house prices based on various features (square footage, location, etc.).")

# def july(request):
#     return HttpResponse("Task: Evaluate the performance of your trained model using metrics like accuracy, precision, recall, and F1 score. Consider techniques like cross-validation for robust evaluation. Example: Evaluate the performance of a spam classification model and tune its hyperparameters for optimal results.")

# def august(request):
#     return HttpResponse("Task: Craft a data-driven story that highlights key findings and recommendations based on your analysis. Prepare presentations or reports to effectively communicate insights to a non-technical audience. Example: Present your findings on customer churn to management, recommending strategies to improve customer retention.")
# def september(request):
#     return HttpResponse("Task: Implement a system to monitor the performance of your deployed model over time. Use techniques like anomaly detection to identify potential issues and retrain the model when necessary. Example: Monitor a fraud detection model for changes in fraud patterns and retrain it periodically to maintain accuracy.")
# def october(request):
#     return HttpResponse("Task: Dedicate time to learn a new data science skill or library. Explore advanced techniques like deep learning, natural language processing, or time series analysis. Online resources like Kaggle Learn, Coursera, or Udacity offer various data science courses. Example: Learn about natural language processing (NLP) techniques to analyze customer reviews and identify sentiment trends.")
# def november(request):
#     return HttpResponse("Task: Collaborate with colleagues on a data science project. Share your code and findings on platforms like GitHub or internal knowledge-sharing platforms. Example: Partner with marketing to analyze customer behavior data and develop targeted marketing campaigns.")
# def december(request):
#     return HttpResponse("Task: Reflect on your accomplishments as a data scientist throughout the year. Review your completed projects and identify areas for improvement for the next year. Example: Analyze the impact of your data science projects on business objectives and set goals for continued growth and learning in the following year.")













# Task: Create compelling data visualizations to effectively communicate insights from your analysis to stakeholders. Use libraries like matplotlib, seaborn, or Plotly for interactive visualization.
# Example: Create interactive dashboards to visualize key business metrics and track progress towards goals.
# August (Data Storytelling & Presentation):

# 
# September (Model Monitoring & Maintenance):

# 
# October (Upskilling & Learning):

# 
# November (Collaboration & Sharing):

# Task: Collaborate with colleagues on a data science project. Share your code and findings on platforms like GitHub or internal knowledge-sharing platforms.
# Example: Partner with marketing to analyze customer behavior data and develop targeted marketing campaigns.
# December (Reflection & Review):

# 