import axios from "axios";
const HOST = 'https://thanhduong.pythonanywhere.com'


//quan ly api
export const endpoints = {
    'categories':'/categories/',
    'courses':'/courses/'
}

// các api cần chứng thực
export const authApi = () => {
    return axios.create({
        baseURL:HOST,
        headers:{
            'Authorization':`Bearer ...`
        }
    })
}

export default axios.create({
    baseURL:HOST
})
