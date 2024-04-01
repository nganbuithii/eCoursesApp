import { View, Text, ActivityIndicator, ScrollView, TouchableOpacity, Image } from "react-native"
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
            <ScrollView style={{flex:1, flexDirection:"row", backgroundColor:"pink"}}>
                {courses === null ? (
                <ActivityIndicator />
                ) : (
                <>
                    {courses.map(course => (
                    <TouchableOpacity key={course.id} style={{flex:3}}>
                        <View>
                            {course.Image ? (
                                <Image source={{uri: course.Image}} style={{width: 100, height: 100}} />
                            ) : (
                                <Text>Không có hình ảnh</Text>
                            )}
                        </View>
                        <Text>{course.subject}</Text>
                    </TouchableOpacity>
                    ))}
                </>
                )}
            </ScrollView>
        </View>
    );
}

export default Home;
