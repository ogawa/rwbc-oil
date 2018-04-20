1, header and foot template are in folder home/header_foot_template, and there are 4 templates, listed as:
  (1) headerEng.html
  (2) headerJp.html
  (3) footJp.html
  (4) footEng.html

2,  python script "gentool.py" will search all of the *.html files in home folder (include sub folders).
    (1) example:    headerJp = ['<!-- BeginOilHeaderJp -->', '<!-- EndOilHeaderJp -->', '../header_foot_template/headerJp.html']
        "gentool.py" will substitute all of the text between <!-- BeginOilHeaderJp --> and <!-- EndOilHeaderJp -->, using ../header_foot_template/headerJp.html.
    (2) there are four types such as
          headerJp = ['<!-- BeginOilHeaderJp -->', '<!-- EndOilHeaderJp -->', '../header_foot_template/headerJp.html']
          footJp = ['<!-- BeginOilFootJp -->', '<!-- EndOilFootJp -->', '../header_foot_template/footJp.html']
          headerEng = ['<!-- BeginOilHeaderEng -->', '<!-- EndOilHeaderEng -->', '../header_foot_template/headerEng.html']
          footEng = ['<!-- BeginOilFootEng -->', '<!-- EndOilFootEng -->', '../header_foot_template/FootEng.html']

3, How to run the script
    (1) go to the working folder "home/tools"
    (2) run script as "python ./gentool.py"

    Note: I have tested this script by python2.7.
