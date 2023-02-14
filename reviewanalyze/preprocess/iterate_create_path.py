# -*- coding: euc-kr -*-

import sys
import io
import os
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class RatingReviewPair:
    def __init__(self, rating, review):
        self.rating = rating
        self.review = review
    
    def get_rating(self):
        return self.rating
    
    def get_review(self):
        return self.review


def return_rating_review_list():
    list_review = []

    path_prefix = "C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\second-trial\\"

    arr = os.listdir(R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\second-trial")

    ex_path = arr[len(arr) - 1]

    for i in arr:
        with open(path_prefix + i, encoding="UTF-8") as file:
            data = json.load(file)
            #result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
            #print(result)
            
            num = data.get("number")
            for i in range(1, num+1):
                rating_review_pair = data.get("review" + str(i))
                print('{}/{}'.format(rating_review_pair[0], rating_review_pair[1]), '\n\n')          
                list_review.append(RatingReviewPair(rating_review_pair[0], rating_review_pair[1]))
        
    print(len(list_review))
    return list_review

if __name__ == "__main__":
    my_list = return_rating_review_list()