* install dependencies: `pip install -r requirements.txt`
* configure your access token to Google Cloud Storage `gsutil config`
  the project-id is the number part of the bucket URL, which is "listed near the bottom of your Reports Reports pages." [1]
* download your favorite CSV from Google Cloud Storage and run: `python markov_gp_review.py <csv_file>`

1: https://support.google.com/googleplay/android-developer/answer/6135870?p=crash_export&rd=1#export
