const state = {
    loading: true,
    course_index: 0,
    data:null

}
var myChart = null, myChart1 = null, myChart2=null;

const update_charts = (course_info) => {
/*
    console.log(course_info)*/
    let canvas = document.getElementById('myChart_pie_status');

    if (canvas) {
        const ctx = canvas.getContext("2d");
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    /*    console.log(myChart);*/
        if (myChart) {
            myChart.destroy();
        }
       myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ["Upcoming", "Completed", "Overdue", "Late"],
                datasets: [{
                    label: '# of Votes',
                    data: Object.keys(course_info["assignments_status"]).map(
                        key => { return course_info["assignments_status"][key] }
                    ),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
           options: {
               responsive: true,
                scales: {

                }
            }
        });
    }



    //[...Array(course_info["number_assignment"]).keys()]
    canvas = document.getElementById('myChart_line_grade');
    if (canvas) {
        const ctx1 = canvas.getContext("2d");
        ctx1.clearRect(0, 0, canvas.width, canvas.height);
        if (myChart1) {
            myChart1.destroy();
        }
         myChart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: course_info["assignments"].map(
                    data => {
                        return data["title"];
                    }
                ),
                datasets: [{
                    label: "Assignment",
                    data: course_info["grades"],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }, {
                        label: 'Average Grade',
                        data: [...Array(course_info["assignments"].length+1).keys()].map(() => course_info["average_grade"]),
                    borderColor: 'rgba(255, 159, 64, 0.2)',
                    backgroundColor: 'rgba(255, 159, 64, 1)',


                }]
            },
             options: {
                 responsive: true,
                scales: {
                    y: {
                        suggestedMin: Math.min(course_info["grades"]) - 10 < 0 ? 0 : Math.min(course_info["grades"]) - 10,
                        suggestedMax: Math.max(course_info["grades"]) + 10 > 100 ? 100 : Math.max(course_info["grades"]) + 10

                    }
                }
            }
        });

    }




}

const onClicked_for_button = (title,index, e) => {
    e.preventDefault();

    const my_buttons = document.getElementById("stv-radio-buttons-wrapper");
    const arr = Array.from(my_buttons.getElementsByTagName("span"));
    for (let index in arr) {

        const span_e = my_buttons.getElementsByTagName("span")[index];
       // span_e.classList.remove("selected");
        span_e.classList.add("selected");
        span_e.className="selected"
        if (span_e.getElementsByTagName("label")[0].innerText == title) {
            my_buttons.getElementsByTagName("span")[index].classList.add("selected");
            console.log(index);
        }
    }
    state.course_index = index;
    update();
}
const create_course_button = (course_title) => {
    const my_buttons = document.getElementById("stv-radio-buttons-wrapper");
    if (my_buttons) {
        my_buttons.innerHTML = "";
        course_title.map((title, index) => {
            my_span = document.createElement("span");
            if (index == state.course_index) {
                my_span.classList.add( "selected" );
            }


            my_span.innerHTML = `
   <label for="button${index}">${title}</label>`;

           // console.log(my_buttons.getElementsByClassName("span"));
            (my_span).addEventListener("click",

                (event) => {

                    onClicked_for_button(title, index, event);

                }
            );
            my_buttons.appendChild(my_span);

        });
    }

}

const create_grade_table = (course_title, course_grade) => {
    const my_table = document.getElementById("myTable_grade");
    //console.log(my_table);
    if (my_table) {
        const table = document.createElement("table");
        table.classList.add("table");
        const table_hd = document.createElement("thead");
        table_hd.classList.add("thead-dark");
        const table_body = document.createElement("tbody");
        const table_tr1 = document.createElement("tr");
        const table_tr2 = document.createElement("tr");
        course_title.map((title, index) => {
            const th = document.createElement("th");
            th.innerText = title
            table_tr1.appendChild(th);

            const td = document.createElement("td");
            td.innerText = course_grade[index];
            table_tr2.appendChild(td);

        });
        table_hd.appendChild(table_tr1);
        table_body.appendChild(table_tr2);

        table.appendChild(table_hd);
        table.appendChild(table_body);
        my_table.appendChild(table);


    }
}
const create_recent_grade = (recent_todos) => {
    const div = document.getElementById("recent_grade");
    if (div) {
        div.innerHTML = "";
        recent_todos.map(todo => {
            const div_ = document.createElement("div");
            div_.classList.add("card_element");
            div_.innerHTML = `<p><a href="/dashboard/todo/${todo.id}">${todo.title}</a> grade: ${todo.grade}</p>`
            div.appendChild(div_);
        })
    }


}
const update_charts_profile = (courses_info) => {
    //console.log(courses_info);
    let canvas = document.getElementById('myChart_radar_grade');
    const course_title = Object.keys(courses_info).map(
        key => {
            return courses_info[key]["course__title"];
        }
    );
    const course_grade = Object.keys(courses_info).map(
        key => {
            return courses_info[key]["average_grade"];
        }
    );
    if (canvas) {
        const ctx2 = canvas.getContext("2d");
        ctx2.clearRect(0, 0, canvas.width, canvas.height);
        if (myChart2) {
            myChart2.destroy();
        }
        myChart2 = new Chart(ctx2, {
            type: 'radar',
            data: {
                labels: course_title,
                datasets: [{
                    label: "course",
                    data: course_grade
                       ,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {

                }
            }
        });
    }

    create_grade_table(course_title, course_grade);
    create_course_button(course_title);
}


const loading = () => {
    let div = document.getElementById("profile_loader");
    if (div) {
        div.innerHTML = ` <div class="loader">Loading...</div>`;
        if (state.loading) {
            div.innerHTML = ` <div class="col-xl-6">
         <div class="card mb-4 my_container">
             <div class="card-header my_header">
                 <i class="fas fa-chart-area mr-1"></i>
                 Courses
             </div>
             <div class="card-body chart_container">
                 <canvas id="myChart_radar_grade" ></canvas>
             </div>
         </div>
     </div>
     <div class="col-xl-6">
         <div class="card mb-4">
             <div class="card-header">
                 <i class="fas fa-chart-area mr-1"></i>
                Grades
             </div>
             <div class="card-body">
                 <div id="myTable_grade">

                 </div>

             </div>
         </div>
     </div>
`
        }
    }
    div = document.getElementById("home_loader");
    if (div) {
        div.innerHTML = ` <div class="loader">Loading...</div>`;
        if (state.loading) {
            div.innerHTML =
                `   <div class="card-header">
                        <i class="fas fa-rss"></i>
                            Assignment Information
                    </div>
                    <div class="card-body">
                        <div id="stv-radio-buttons-wrapper"></div>
                    </div>
                    <div class=container-fluid>
                        <div class="row">
                            <div class="col-xl-6">
                                <div class="card mb-4 my_container">
                                    <div class="card-header my_header">
                                        <i class="fas fa-chart-area mr-1"></i>
                                        Recent Grades
                                    </div>
                                    <div class="card-body chart_container">
                                        <canvas id="myChart_line_grade" width="200" height="200"></canvas>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6">
                                <div class="card mb-4 my_container">
                                    <div class="card-header my_header">
                                        <i class="fas fa-chart-area mr-1"></i>
                                        Assignment Progress
                                    </div>
                                    <div class="card-body chart_container" >
                                        <canvas id="myChart_pie_status" width="200" height="200"></canvas>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    `

        }
    }




}
const update = () => {
    state.loading = true;
    loading();
    update_charts(state.data[state.course_index]);
    update_charts_profile(state.data);

}
state.loading = false;
loading();
console.log(window.location.origin);
axios.get(window.location.origin+"/profile/get_data").then(
    response => {

/*        console.log(response.data);
        console.log(response.data.recent);*/
        state.data = response.data.data;
        update();
        create_recent_grade(response.data.recent);

    }

).catch(e=>{


  console.log(e);
});
