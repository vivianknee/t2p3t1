---
layout: post
author: VASE
title: Trimester 1 Project
---

<html lang="eng">
<head>
    <meta charset ="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body id="button">
    <div>
        <div class="vertical-center">
         <h1>VASE Diagnosis System</h1>
        </div>
        <div class="vertical-center">
            <BUTTON class="instructbtn" ONCLICK="ShowAndHide()">View Instructions Here</BUTTON>
            <div ID="Instructions" STYLE="display:none">Welcome to our VASE Diagnosis System. This system will help provide you with a diagnosis. All you need to do is select the symptoms you might have with the checkboxes below. Then click the 'Get Diagnosis' button at the bottom, and you'll receive a report on the condition you might have, steps to take in the future, as well as an option to get the report sent to your email.</div>
        </div>
        <hr>
            <table class="table-latitude">
                <thead>
                    <tr>
                        <th>Symptoms</th>
                        <th>Check what Applies</th>
                    </tr>
                    </thead>
                    <tbody id="result">
                    </tbody>
            </table>
    </div>
    <div class="vertical-center">
        <BUTTON id="btn_get_diagnosis" class="instructbtn">Get Diagnosis</BUTTON>
    </div>
    <p id="output"></p>
</body>
</html>

 <script> 
    sympDict = {};

    const resultContainer = document.getElementById("result");

    const btnDiag = document.getElementById("btn_get_diagnosis");
    
    const url = "https://vase.nighthawkcodescrums.gq/api/diagnosis/";

    const options = {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'no-cors', // no-cors, *cors, same-origin
        cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'omit', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
    };
    // prepare fetch PUT options, clones with JS Spread Operator (...)
    const put_options = {...options, method: 'PUT'}; // clones and replaces method

    btnDiag.addEventListener('click', (event) => {
        sympStr = "";
        for (const s in sympDict) {
            if (sympDict[s]) {
                sympStr = sympStr + s + ", ";
            }
        }

        fetch(url+"diagnosis", options)
            .then(response => {
                if (response.status !== 200) {
                    //error('GET API response failure: ' + response.status);
                    return;
                }
                // valid response will have JSON data
                response.json().then(output => {
                    document.getElementById('output').innerHTML = JSON.stringify(output);
                    console.log(output);
                })
            })
    })

    // fetch the API
    fetch(url+"symptoms", options)
        // response is a RESTful "promise" on any successful fetch
        .then(response => {
            // check for response errors
            if (response.status !== 200) {
                error('GET API response failure: ' + response.status);
                return;
            }
            // valid response will have JSON data
            response.json().then(data => {
                console.log(data);

                    for (const symptom of data){
                        console.log(symptom);
                    
                        const tr = document.createElement("tr");
                    
                        const symptom_ele = document.createElement("td");
                        symptom_ele.innerHTML = symptom.toString();

                        const status = document.createElement("td");
                        var x = document.createElement("INPUT");
                        x.setAttribute("type", "checkbox");
                        x.setAttribute("id", symptom.toString());
                        x.setAttribute("class", "cell-center");

                        x.addEventListener('click', (event) => {
                            if (event.currentTarget.checked == true) {
                                sympDict[symptom] = true;
                                console.log(event.currentTarget.id);
                            } else {
                                console.log('you unchecked this box')
                                sympDict[symptom] = false;
                            }
                        })

                        status.appendChild(x);

                    // this builds ALL td's (cells) into tr element
                        tr.appendChild(symptom_ele);
                        tr.appendChild(status);
                        resultContainer.appendChild(tr);
                    }
        
                })
            })

    function ShowAndHide() {
        var instruct = document.getElementById('Instructions');
        if (instruct.style.display == 'none') {
            instruct.style.display = 'block';
        } else {
            instruct.style.display = 'none';
        }
    }
 </script>
