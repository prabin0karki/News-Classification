from nltk.corpus import stopwords
from sklearn.datasets import load_files
import re

dataset = load_files('Agriculture')

X,y = dataset.data,dataset.target
    
corpus = []
for i in range(0, len(X)):
    review = re.sub(r'\W', ' ', str(X[i]))
    review = review.lower()
    review = re.sub(r'^br$', ' ', review)
    review = re.sub(r'\s+br\s+',' ',review)
    review = re.sub(r'\s+[a-z]\s+', ' ',review)
    review = re.sub(r'^b\s+', '', review)
    review = re.sub(r'\s+', ' ', review)
    corpus.append(review)    
       
       
# Creating the BOW model
#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
#X = vectorizer.fit_transform(corpus).toarray()    
#    
# Creating the Tf-Idf model 
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = None,min_df =0.001, max_df = 0.70, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()
    
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.01, random_state = 0)    


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train, y_train)

print("Please provide us with your problem.")
value = input("")
prediction = clf.predict(vectorizer.transform([value]))
def predict():
    if prediction==0:
        print("Your problem might be: Alternate Year Bearing. The solution to this is :")
        print("The application of Sugar Mover to the whole plant every 10 days will cause the leaves to synthesize more photosynthates (sugar) and will cause the leaves to transfer more of these to the sugar reserves in the woody tissue of the plant. <br> This application should begin immediately after fruit set. It should be continued on a 10 day interval until harvest. If this is done in consistent manner, it will help create the sugar reserves in the woody tissue so that there is adequate food for the large developing crop, shoot growth, root growth, and the developing buds for next year’s crop.If the above treatment is followed, the bud primorida should remain healthy every year. The amount of alternate year bearing should be greatly reduced. One may then have more consistent yields every year.")


    
    elif prediction==1:
        print("Your problem might be :Drought. The solution to this is:")
        print(" Foliar spray 1.0 pint per acre of Bio-Forge when stress is normally seen in the field. This is a single application per season. This application should last inside the plant for the duration of the annual growth.When the plant is sprayed with Bio-Forge, the leaves will unroll and the plant will turn a darker green. This should occur within 6 days after the application is made.Another feature of Bio-Forge will enable the grower to use less irrigation water. If plant cells are kept clean so that they can synthesize more water in the living tissue, less irrigation water will be needed in order to observe more normal plant growth.As water becomes less and less available and the pumping cost of water becomes greater, due to energy costs, the reduction of irrigation water on a yearly basis, will be more important than just maintaining of the plant from drought stress and loss of yield. ")


    elif prediction==2:
        print("Your problem might be : Grain Size.The solution to this is: ") 
        print("The application of Bio-Forge at flag leaf emergence will enable the plant to hormonally pass through the problem area of change from vegetative to reproductive. The application of Bio-Forge will tend to reduce the ethylene and abscisic acid formation, which causes root growth to cease and plant tissue to die.This is a simple application that can be applied by a ground spray or aerial application.Bio-Forge should greatly reduce the negative effect caused by drought, high temperatures and the lack of sunlight to a full part of the plant.")  
    
    elif prediction==3:
        print("Your problem may be: Lack of flower. The solution to this is:")
        print("The application of 2 quarts per acre of Load will accomplish the above purpose. It should be foliar applied to any tree with vigorous growth approximately 2 weeks before anticipated bud swell. This should cause a hormonal shift in a tree so that the buds will tend to come out of dormancy and set flowers.The same principal applies to annual crops that have difficulty setting flowers. It will also apply to annual crops that have vigorous shoot growth before the normal period of flowering. This would apply to such crops as soybeans, canola, tomatoes, or any other multiple fruiting crop where excessive nitrogen has been used or growing conditions are conductive to rapid vegetative growth.On non-tree crops, the increase of budding and flowering may be accomplished by foliar application of only 1 quart per acre of Load.Buds can be forced out of any plant during the reproductive stage of growth. In order to maximize the value of this foliar treatment, however, it should be applied just before the bud swell period on any crop.")
    
    elif prediction==4:
        print("Your problem may be:PLant Growth. The solution to this is:")    
        print("The application of Bio-Forge at the rate of 1.0 pint per acre on soybeans at the R4.5 to R5.0 stage of development, will maintain plant health, vigor and increase the amount of sugar transport from the leaves to the developing pods and seeds.The application of Bio-Forge at the rate 1.0 pint per acre on corn at the V12 stage (approximately 1 week before tassel shows) will increase the plant vigor, even during drought situations. It does so by regulating the hormone balance in the corn plant. The plant will maintain more auxin for pollen viability and will reduce the level of ABA in the developing ear. Ear size will be larger and the number of viable kernels on the ear will increase. Also, the kernel size will be greater.The above treatments on both soybeans and corn are designed to maintain plant health in the latter stages of growth in order to maximize yields of both crops.") 
    
    elif prediction==5:
        print("Your problem may be due to Micronutrient in plants. The solution to this is:")   
        print("Apply 1.0 quart per acre of X-Tra Power in the furrow at planting time. This will provide the micronutrients which normally show up in instances where glyphosate may retard cell division.X-Tra Power will also cause the roots to make and accumulate more auxin. This gives the plant a double defense against any possibility of glyphosate interrupting cell division.If one is not able to place an infurrow application of X-Tra Power or place an application of X-Tra Power with starter fertilzer, the alternative is to spray 1.0 quart of X-Tra Power on the foliage when the plant has approximately 3-4 leaves.If X-Tra Power is used as a soil treatment at planting or used as a foliar spray when plants have 3-4 leaves, any problems of cell division at the root tips should be overcome.The only better treatment than above, is to use 1.0 quart of X-Tra Power in the soil at planting, plus 1.0 quart of X-Tra Power at the V3 to V4 leaf state. The combination will give greater yield increases and even help the plant become more resistant to sucking insects, such as aphids")
    
    elif prediction==6:
        print("Your problem may be lack of Pollination. The solutio to this might be:")
        print("It is very simple to supply adequate auxin to each flower. The application of 3 pints of Flower Power to the plant during the period of when there is approximately 10% appearance of flowers on the plant. This should supply sufficient auxin for both the flowers that are present and the developing buds which will become flowers. The application of Flower Power will guarantee that there should be sufficient auxin so that during periods of temperature extremes, there should be enough auxin in the flower for stronger pollination.The application of Flower Power in order to increase the power of pollination needs only to be done one time. If there is a weak plant or plants with a prolonged period of flowering, a second application may need to be done 10 days after the first application.")

    
    elif prediction==7:
        print("Your problem may be due to insects. The solution to this might be: ")
        print("The protection of a plant, using its natural defense system, is very simple. The application of X-Tra Power every 7 days should help a plant produce and maintain sufficient auxin in order to make it resistant to sucking insects. The rate would be 1 quart per acre. Since auxin has a very short half-life, this treatment needs to be applied every 7 days.X-Tra Power may be used by itself or it may be used along with a chemical that is reported to help control sucking insects. Many of the sucking insects, however, have become resistant to the insecticides which once controlled sucking insects. This is particularly true on crops such as onions.The easiest way to control the feeding of sucking insects on the plant is to use the plant’s natural defense mechanism which discourages the sucking insects from feeding on the plant’s new leaf tissue.")
    
    elif prediction==8:
        print("Your problem may be summer drop in fruits. The solution might be:")   
        print("Apply 1.5 to 2.0 pints per acre of Bio-Forge as a foliar application approximately 2 weeks before the summer nut drop season is common. Bio-Forge has the ability to up regulate auxin and auxin transport into the fruit during this change from the liquid state into the seed embryo state. The use of Bio-Forge will greatly reduce the summer fruit drop on any tree. The timing, however, is very important. It must be applied approximately 2 weeks before the liquid stage begins the development of the seed embryo stage inside the fruit.When considering citrus, the seed in the citrus fruit will determine the time of summer fruit drop. The seed inside the citrus fruit will also pass from a liquid stage into an embryonic or solid stage. It is during this transition period that citrus will experience summer drop.")         
    

predict()    
    
