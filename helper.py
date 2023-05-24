import pdfplumber


def extract_data(feed):
    data = []
    full_text = None
    if feed.type == 'application/pdf':
        with pdfplumber.open(feed) as pdf:
            all_text = []
            for each_page in pdf.pages:
                all_text.append(each_page.extract_text(x_tolerance=3,
                                                       y_tolerance=3,
                                                       layout=False,
                                                       x_density=7.25,
                                                       y_density=13).replace('\n', ' '))
        full_text = " ".join(all_text)
    elif feed.type == 'text/plain':
        full_text = feed.getvalue().decode("utf-8")
    return full_text