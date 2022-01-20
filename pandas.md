# Group and count columns by different categories.

each column contains the count for each category


'''
data = df.groupby("image_remote_id").apply(
          lambda x: x["conclusion"].value_counts()[df["conclusion"].cat.categories]
      ).to_numpy()
'''
