function checkpwd(){
    response = false;
    var pwd =  $("#password").val();
    var conpwd = $("#conpassword").val();
    if(pwd == conpwd){
        return true;
    }
    alert('Password and Confirm Password does not match.');
    return response;
}
var cities = ["Bhandup", "Mumbai", "Visakhapatnam", "Ahmedabad", "Delhi", "Bangalore", "Pune", "Nagpur", "Panvel","Vadodara",
          "Indore", "Ulhasnagar", "Bhopal", "Kolkata", "Kanpur", "New Delhi", "Kalyan", "Rajkot", "Ghaziabad","Chennai",
          "Meerut", "Agra", "Jaipur", "Jabalpur"];
var citystat =[0.60, 8.77, 1.75, 0.88, 10.52, 7.01, 9.64, 4.38, 1.23, 2.10, 5.96, 3.68, 4.03, 2.98,
                2.10, 5.96, 2.28, 1.05, 6.49, 4.38, 1.58, 4.91, 2.10, 5.61];

var Sex = ["Male", "Female"];
var Sexstat = [59.81,40.19]
var Vehicles = ["Bike","Car","Bus","Truck","Rickshaw"];
var Vehiclesstat =[41.69,21.82,11.07,9.44,15.96]
var activities = ['traffic-accidents', 'Whether condition' , 'Rash Driving' , 'Heavy rain' , 'U-turn' ,'Air-polution'];
var activitiesstat = [22.64,18.45,10.85,28.97,8.01,11.77];

var CityWiseData = [];
var Vehiclewise =[];
var GenderWise =[];
var Accident_issueswise = [];
function Loadfoamtree() {

var foamtree = new CarrotSearchFoamTree({id: "Visulization"})
var foamtree1 = new CarrotSearchFoamTree({id: "Visulization1"})
var foamtree2 = new CarrotSearchFoamTree({id: "Visulization2"})
var foamtree3 = new CarrotSearchFoamTree({id: "Visulization3"})
CityWiseData =[];
Vehiclewise =[];
GenderWise =[];
Accident_issueswise = [];
JSONdata();
       foamtree.set({
            dataObject: {
                groups: CityWiseData
            },
            titleBarDecorator: function (options, parameters, variables) {
                variables.titleBarShown = true;
                variables.titleBarText = (parameters.group.label1 == null) ? '' + "Weightage " + (parameters.group.weight).toFixed(2) + "%" : parameters.group.label1 + ": Weightage " + (parameters.group.weight).toFixed(2) + "%";
            },
            fadeDuration: 500
        });
        foamtree1.set({
            dataObject: {
                groups: Vehiclewise
            },
            titleBarDecorator: function (options, parameters, variables) {
                variables.titleBarShown = true;
                variables.titleBarText = (parameters.group.label1 == null) ? '' + "Weightage " + (parameters.group.weight).toFixed(2) + "%" : parameters.group.label1 + ": Weightage " + (parameters.group.weight).toFixed(2) + "%";
            },
            fadeDuration: 500
        });
        foamtree2.set({
            dataObject: {
                groups: GenderWise
            },
            titleBarDecorator: function (options, parameters, variables) {
                variables.titleBarShown = true;
                variables.titleBarText = (parameters.group.label1 == null) ? '' + "Weightage " + (parameters.group.weight).toFixed(2) + "%" : parameters.group.label1 + ": Weightage " + (parameters.group.weight).toFixed(2) + "%";
            },
            fadeDuration: 500
        });
        foamtree3.set({
            dataObject: {
                groups: Accident_issueswise
            },
            titleBarDecorator: function (options, parameters, variables) {
                variables.titleBarShown = true;
                variables.titleBarText = (parameters.group.label1 == null) ? '' + "Weightage " + (parameters.group.weight).toFixed(2) + "%" : parameters.group.label1 + ": Weightage " + (parameters.group.weight).toFixed(2) + "%";
            },
            fadeDuration: 500
        });
    }

function JSONdata() {
            for (var i = 0; i < cities.length; i++) {
                var temp = {
                    "label": cities[i] + ' (' + parseFloat(citystat[i]).toFixed(2) + '%)',
                    "label1": cities[i],
                    "weight": citystat[i]
                }
                CityWiseData.push(temp);
            }
            for (var i = 0; i < Vehicles.length; i++) {
                var temp = {
                    "label": Vehicles[i] + ' (' + parseFloat(Vehiclesstat[i]).toFixed(2) + '%)',
                    "label1": Vehicles[i],
                    "weight": Vehiclesstat[i]
                }
                Vehiclewise.push(temp);
            }
            for (var i = 0; i < Sex.length; i++) {
                var temp = {
                    "label": Sex[i] + ' (' + parseFloat(Sexstat[i]).toFixed(2) + '%)',
                    "label1": Sex[i],
                    "weight": Sexstat[i]
                }
                GenderWise.push(temp);
            }
            for (var i = 0; i < activities.length; i++) {
                var temp = {
                    "label": activities[i] + ' (' + parseFloat(activitiesstat[i]).toFixed(2) + '%)',
                    "label1": activities[i],
                    "weight": activitiesstat[i]
                }
                Accident_issueswise.push(temp);
            }
 }
 function checkform(){
    response = true;
    var Age =  $("#Age").val();
    var Speedlimit = $("#Speedlimit").val();
    if(Age != undefined && Age != null && Age != ""){
        if(Age > 75){
            alert('Age cannot be greater than 75');
            return false
        }
        if(Age < 21){
            alert('Age cannot be less than 21');
            return false
        }
    }
    else{ alert('Please enter the Age of Driver');return false}
      if(Speedlimit != undefined && Speedlimit != null && Speedlimit != ""){
        if(Speedlimit > 75){
            alert('Speedlimit cannot be greater than 120');
            return false
        }
        if(Speedlimit < 20){
            alert('Speedlimit cannot be less than 20');
            return false
        }
    }
    else{ alert('Please enter the Speedlimit');return false}
    return response;
 }