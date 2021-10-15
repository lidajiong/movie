import pandas as pd
from datetime import datetime
#-------csv文件地址信息-------------------------------
user_dir = '/home/lisha/PycharmProjects/zy/dazuoye/ml-25m/tags.csv'
movie_dir = '/home/lisha/PycharmProjects/zy/dazuoye/ml-25m/movies.csv'
genre_dir = '/home/lisha/PycharmProjects/zy/dazuoye/ml-25m/movies.csv'
link_dir = '/home/lisha/PycharmProjects/zy/dazuoye/ml-25m/links.csv'
rating_dir = '/home/lisha/PycharmProjects/zy/dazuoye/ml-25m/ratings.csv'
#-----------------1、一共有多少不同用户--------------------
def user_number (dir):
    user_data = pd.read_csv(dir)  # 读取训练数据
    t=user_data.duplicated(subset=["userId"],keep=False)
    n_user=len(t[t==False])#False的个数即代表不重复的键的个数
    print("user_number is :",n_user)

#-----------------2、一共有多少不同电影--------------------
def movie_number (dir):
    movie_data = pd.read_csv(dir)  # 读取训练数据
    t=movie_data.duplicated(subset=["movieId"],keep=False)
    n_movie=len(t[t==False])#False的个数即代表不重复的键的个数
    print("movie_number is :",n_movie)

#-----------------3、一共有多少电影类型--------------------
def genre_number (dir):
    genre_data = pd.read_csv(dir)  # 读取训练数据
    genress = genre_data["genres"].str.split(pat="|")
    #print(aaaa[0].tail(20))
    genres = pd.Series([genre for _, genre_list in genress.items() for genre in genre_list],
                       name="genres")  # 所有体裁组成一个list（包含重复）
    genres = genres.unique().tolist()
    genres.remove('(no genres listed)')  # ! 认为没有题材不算一个题材，如果认为算，删掉此行即可
    print("genre_number is :",len(genres))

#-----------------4、没有外部链接的电影数-----------------------------
def link_number (link_dir,movie_dir):
    link_data = pd.read_csv(link_dir)  # 读取训练数据
    movie_data = pd.read_csv(movie_dir)
    he_data = pd.merge(link_data, movie_data)
    print("The number of movies without external links is :",(he_data["tmdbId"].isna().sum()+he_data["imdbId"].isna().sum()))

#-----------5、2018年对电影进行过评分的人数-----------------------------------------------
def rating_number (dir):
    rating_data = pd.read_csv(dir)  # 读取训练数据
    #print(rating_data.tail(20))
    start_time = datetime(2018, 1, 1, 0, 0).timestamp()
    end_time = datetime(2019, 1, 1, 0, 0).timestamp() - 1
    #time_data = rating_data.loc[(rating_data.timestamp >= 1514764800) & (rating_data.timestamp <= 1567850400)]
    time_data = rating_data.loc[(rating_data.timestamp >= start_time) & (rating_data.timestamp <= end_time)]
    t = time_data.duplicated(subset=["userId"], keep=False)
    n_time = len(t[t == False])
    print("taring_number in 2018 is :", n_time)

if __name__ == "__main__":

    user_number (user_dir)
    movie_number (movie_dir)
    genre_number (genre_dir)
    link_number (link_dir,movie_dir)
    rating_number (rating_dir)

