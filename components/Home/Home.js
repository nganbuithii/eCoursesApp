import { View, Text, ActivityIndicator } from "react-native"
import MyStyles from "../../Styles/MyStyles"
import Styles from "./Styles"
import React, { useEffect, useState } from "react"
import API, { endpoints } from "../../Configs/API"

const Home = () => {
    const [courses, setCourses] = React.useState(null);
    
    // Fetch API
    React.useEffect(() => {
        const loadCourses = async() =>{
            try {
                
                let res = await API.get(endpoints['courses']);
                //console.log(res.data.results)
                setCourses(res.data.results);
            } catch(ex) {
                console.error(ex);
            } 
        }

        loadCourses();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={Styles.subjects}>HOME - Trang chủ</Text>

            {/* Sử dụng ActivityIndicator khi đang tải dữ liệu */}
            {courses === null ? (
            <ActivityIndicator />
            ) : (
            <>
                {courses.map(course => (
                <View key={course.id}>
                    <Text>{course.subject}</Text>
                </View>
                ))}
            </>
            )}
        </View>
    );
}

export default Home;
