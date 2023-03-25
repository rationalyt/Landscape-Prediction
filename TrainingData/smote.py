from data_collect import merge_files
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score
from sklearn.model_selection import train_test_split


dict= {1:8, 2:5, 3:3, 4:2, 5:3 ,6:3, 7:4, 8:1 }

rf = RandomForestClassifier(n_estimators=40)
for i in dict.keys():
    for j in range(1,dict[i]+1):
        XInput = "subject_00"+str(i)+"_0"+str(j)+"__x.csv"
        YInput = "subject_00"+str(i)+"_0"+str(j)+"__y.csv"
        # print(XInput)
        # print(YInput)
        # print("\n")
        output_df = merge_files(XInput,YInput)

        X,y = output_df[['a1','a2','a3','g1','g2','g3']],output_df['y']
        y = y.fillna(0)
        y = y.astype(int)

        # print(type(X.iloc[0,0]))
        # print(X.head())
        # print(y.head())
        # counter = Counter(y)
        # print(counter)
        oversample = SMOTE(random_state=1)
        balanced_X, balanced_y = oversample.fit_resample(X, y)
        #print(balanced_X)
        #print(balanced_y)
        counter = Counter(balanced_y)
        # print(counter)

        X_train, X_test, y_train, y_test = train_test_split(balanced_X,balanced_y,test_size=0.2)


        rf.fit(X_train, y_train)
        y_output = rf.predict(X_test)
        print(y_output)
        print(rf.score(X_test, y_test))
        print(f1_score(y_test,y_output,average='weighted'))
        print(precision_score(y_test,y_output,average='weighted'))
        print(accuracy_score(y_test,y_output))


