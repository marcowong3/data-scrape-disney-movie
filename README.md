# Disney Movie Data Scrape
In this project, I complete steps to create a dataset from scratch and utilize it to predict Box Office revenue. The dataset contains all the information found on each Disney movies' Wikipedia information box.
<br /> <br /> Movie List: https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films

## Libraries/Helpers
- Data Scraping: BeautifulSoup, Requests
- Save/Load Files: JSON, Pickle, CSV, Pandas
- API: The Open Movie Database (http://www.omdbapi.com)
- Plotting/Modelling: matplotlib, seaborn, scikit-learn
- Others: urllib, os, datetime, RegEx

Pytest from [helper](https://github.com/marcowong3/scrape-disney-movie/tree/main/helper) was used in Task 3 to convert monetary strings to numerical values

##  Dataset Creation Tasks Outline
Task 1: Build a script to access the information box found on a movie's Wikipedia page.  <br/>
Task 2: Build a script to access all movies' information box found in Movie List url. <br/>
Task 3: Clean Data, Test Code with Pytest <br/>
Task 4: Attach IMDB/Rotten Tomatoes/Metascore Scores <br/>
Task 5: Remove Junk Columns <br/>
Task 6: Save final data as CSV/Pickle <br/>

The final datasets ready for analysis are formatted as CSV and Pickle are found at [this folder](https://github.com/marcowong3/scrape-disney-movie/tree/main/disney_data_final) <br/>

##  Dataset Analysis Tasks Outline
- Data Exploration
- Statistical Analysis
- Box Office Modelling (Using Running time, Budget,	imdb,	Metascore,	RottenTomato,	Release Year)

## Result
<img src="./predicted_vs_actual.png">
