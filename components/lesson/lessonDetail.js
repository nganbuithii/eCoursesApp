import { View, Text } from "react-native"
import MyStyles from "../../Styles/MyStyles"
import React, { useEffect } from "react";

const LessonDetail = ({route}) => {
    const {lessonId} = route.params;

    useEffect(() => {
        // chi tiết trả ra đối tượng
        const loadLesson = async()=>{
            
        }
    },[lessonId])

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>CHI TIẾT BÀI HỌC</Text>
        </View>
    )
}

export default LessonDetail;