import { View, Text, ScrollView, ActivityIndicator, TouchableOpacity, Image } from "react-native";
import MyStyles from "../../Styles/MyStyles";
import react, { useEffect, useState } from "react";
import API, { endpoints } from "../../Configs/API"

const Lesson = ({route, navigation}) => {
    // NẠP API
    // b1: Gắn đối số route
    // b2 khai 

    const {courseId} = route.params;
    const [lessons, setLessons] = useState(null); 

    useEffect(() => {
        const loadLesson = async () => {
            try{
                let res = await API.get(endpoints['lessons'](courseId));
                // không phân trang nên lấy nguyên dữ liệu
                setLessons(res.data);
            }catch(ex){
                console.error(ex);
            }
        }
        loadLesson();
    },[courseId])

    const goToDetails = (lessonId) => {
        navigation.navigate("LessonDetail", {"lessonId": lessonId})
    }

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>
                DANH SÁCH BÀI HỌC
            </Text>

            {/* Nếu những đoạn code lặp đi lặp lại nên tách thành component riêg */}
            <ScrollView style={{flex:1, flexDirection:"row", backgroundColor:"pink"}}>
                {lessons === null ? (
                <ActivityIndicator />
                ) : (
                <>
                    {lessons.map(lesson => (
                    <TouchableOpacity onPress={() => goToDetails(lesson.id)} key={lesson.id} style={{flex:3}}>
                        <View style={[MyStyles.row, {backgroundColor:"yellow"}]}>
                            <Image source={{uri: lesson.image}} style={{width: 100, height: 100}} />
                            <View style={MyStyles.row}>
                                <Text>{lesson.subject}</Text>
                            </View>
                        </View>
                    
                        
                    </TouchableOpacity>
                    ))}
                </>
                )}
            </ScrollView>
        </View>
    )
}

export default Lesson;