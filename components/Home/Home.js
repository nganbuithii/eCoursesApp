import { View, Text, ActivityIndicator, ScrollView, TouchableOpacity, Image } from "react-native"
import MyStyles from "../../Styles/MyStyles"
import Styles from "./Styles"
import React, { useEffect, useState } from "react"
import API, { endpoints } from "../../Configs/API"

const Home = ({route, navigation}) => {
    const [courses, setCourses] = React.useState(null);
    const cateId = route.params?.cateId;
    
    // Fetch API
    React.useEffect(() => {
        const loadCourses = async() =>{
            let url = endpoints['courses']
            if (cateId !== undefined && cateId != null)
                url = `${url}?category_id=${cateId}`
            try {
                
                let res = await API.get(url);
                //console.log(res.data.results)
                setCourses(res.data.results);
            } catch(ex) {
                console.error(ex);
            } 
        }

        loadCourses();
        // Nếu CateId thay đổi thì sẽ fetch lại dữ liệu
    }, [cateId]);


    // Xử lí chuyển trang
    const goToLesson = (courseId) => {
        navigation.navigate("Lesson", {"courseId":courseId})
    }

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
                    <TouchableOpacity onPress={() => goToLesson(course.id)} key={course.id} style={{flex:1}}>
                        <View style={[MyStyles.row]}>
                            <Image source={{uri: course.image}} style={MyStyles.img} />
                            <View style={MyStyles.row}>
                                <Text style={{marginLeft: 10}}>{course.subject}</Text>
                            </View>
                        </View>
                
                </TouchableOpacity>
                    ))}
                </>
                )}
            </ScrollView>
        </View>
    );
}

export default Home;
