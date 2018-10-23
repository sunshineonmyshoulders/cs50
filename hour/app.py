from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html") 

@app.route("/result", methods=["GET", "POST"])
def result():
	h1 = int(request.form.get("h1"))
	m1 = int(request.form.get("m1"))
	s1 = int(request.form.get("s1"))
	h2 = int(request.form.get("h2"))
	m2 = int(request.form.get("m2"))
	s2 = int(request.form.get("s2"))

	h_result = h1 + h2
	m_result = m1 + m2
	s_result = s1 + s2
	d_result = 0

	if s_result >= 60:
		s_result-= 60
		m_result+= 1

	if m_result >= 60:
		m_result-= 60
		h_result+= 1

	if h_result > 24:
		h_result-= 24
		d_result+= 1
	return render_template("result.html", h1=h1, m1=m1, s1=s1, h2=h2, m2=m2, s2=s2, rh=h_result, rm=m_result, rs=s_result, d=d_result )