/** 
 * Variables
 * 
 * These variables must be updated every three days to
 * match new machine learning predictions. Run 
 * "Official Main Algorithm.py" to get new temperatures.
*/

var atl_data = {
    temps : ["60.99","70.77","62.99"],
    warn : ["No Warnings","All is well."]
};

var col_data = {
    temps : ["48.11","64.05","53.29"],
    warn : ["No Warnings","All is well."]
};

var chr_data = {
    temps : ["57.75","46.61","75.52"],
    warn : ["No Warnings","All is well."]
};

/**
 * Button Functions and Initial Display
 * 
 * These are functions that will display the information;
 * chart and variables. 
 * 
 * Note: Charts also need to be updated as well. Export data 
 * from .csv files along with prediction data to make an
 * appropriate chart via Excel or Graphing Program.
 */

function display_init_info(){
    var place_init_chart = document.getElementById("weather_chart")
    place_init_chart.innerHTML="<img width=100% height=100% src=\"images/p_model_atl.png\">"
    display_temp1.innerHTML = atl_data['temps'][0]+" Degrees Farienheight"
    display_temp2.innerHTML = atl_data['temps'][1]+" Degrees Farienheight"
    display_temp3.innerHTML = atl_data['temps'][2]+" Degrees Farienheight"
    past_data.innerHTML = "<img width=50% height=50% src=\"images/2w_atl.png\">"
    display_emergency.innerHTML = "<p>"+atl_data['warn'][0]+"</p><p>"+atl_data['warn'][1]+"</p>"
}

function display_atl_info(){
    var weather_chart = document.getElementById("weather_chart")
    weather_chart.innerHTML="<img width=100% height=100% src=\"images/p_model_atl.png\">"
    display_temp1.innerHTML = atl_data['temps'][0]+" Degrees Farienheight"
    display_temp2.innerHTML = atl_data['temps'][1]+" Degrees Farienheight"
    display_temp3.innerHTML = atl_data['temps'][2]+" Degrees Farienheight"
    past_data.innerHTML = "<img width=50% height=50% src=\"images/2w_atl.png\">"
    display_emergency.innerHTML = "<p>"+atl_data['warn'][0]+"</p><p>"+atl_data['warn'][1]+"</p>"
}

function display_col_info(){
    var weather_chart = document.getElementById("weather_chart")
    weather_chart.innerHTML="<img width=100% height=100% src=\"images/p_model_col.png\">"
    display_temp1.innerHTML = col_data['temps'][0]+" Degrees Farienheight"
    display_temp2.innerHTML = col_data['temps'][1]+" Degrees Farienheight"
    display_temp3.innerHTML = col_data['temps'][2]+" Degrees Farienheight"
    past_data.innerHTML = "<img width=50% height=50% src=\"images/2w_col.png\">"
    display_emergency.innerHTML = "<p>"+col_data['warn'][0]+"</p><p>"+col_data['warn'][1]+"</p>"
}

function display_chr_info(){
    var weather_chart = document.getElementById("weather_chart")
    weather_chart.innerHTML="<img width=100% height=100% src=\"images/p_model_chr.png\">"
    display_temp1.innerHTML = chr_data['temps'][0]+" Degrees Farienheight"
    display_temp2.innerHTML = chr_data['temps'][1]+" Degrees Farienheight"
    display_temp3.innerHTML = chr_data['temps'][2]+" Degrees Farienheight"
    past_data.innerHTML = "<img width=50% height=50% src=\"images/2w_chr.png\">"
    display_emergency.innerHTML = "<p>"+chr_data['warn'][0]+"</p><p>"+chr_data['warn'][1]+"</p>"
}