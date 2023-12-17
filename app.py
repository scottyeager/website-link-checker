from flask import Flask, request, jsonify
from website_link_checker import check_links

app = Flask(__name__)

@app.route('/<path:url>')
def report(url):
    if url == 'favicon.ico':
        return ''

    print('checking links for: ' + url)
    filtered_data, has_error, muffet_links, muffet_start, muffet_end, retry_start, retry_end = check_links(url, 'all', '', False)
    print('filtered data: ' + str(filtered_data))

    if filtered_data:
        response = jsonify(filtered_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return 'No errors found, woohoo!'