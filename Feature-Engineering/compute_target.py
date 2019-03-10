sample = pd.read_csv("/Users/gracezhang/Desktop/leanplum/sample_submission_2.csv")
user_df = pd.DataFrame(sample["user_id_hash"])
features.rename(columns={'user_id':'user_id_hash'}, inplace=True)
features_new = features[["user_id_hash", "avg_previous_sessions_duration", "num_of_session", "region", "month", "day_of_week"]]

df_join = sample[["user_id_hash"]].join(features_new.set_index('user_id_hash'), on='user_id_hash', how="left")

X_test = df_join.drop("user_id_hash", axis=1)

# Get the most common value for month, region, and dow
X_test['month'].value_counts().idxmax()
X_test['region'].value_counts().idxmax()
X_test['day_of_week'].value_counts().idxmax()

X_test["avg_previous_sessions_duration"].fillna(0, inplace=True)
X_test["num_of_session"].fillna(0, inplace=True)
X_test["month"].fillna(0.0, inplace=True)
X_test["region"].fillna(1.0, inplace=True)
X_test["day_of_week"].fillna(0.0, inplace=True)

prediction_one_week = rf.predict_proba(X_test)
prediction_two_week = rf_2.predict_proba(X_test)

submission = pd.concat([user_df, pd.DataFrame(prediction_one_week[:,-1]), pd.DataFrame(prediction_two_week[:,-1])], axis=1)

submission.columns = ["user_id_hash", "user_purchase_binary_7_days", "user_purchase_binary_14_days"]

sample.loc[:, 'user_purchase_binary_7_days'] = submission['user_purchase_binary_7_days'] 
sample.loc[:, 'user_purchase_binary_14_days'] = submission['user_purchase_binary_14_days']
sample.to_csv('/Users/gracezhang/Desktop/submission.csv',index=False)