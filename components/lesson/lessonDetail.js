import { View, Text, ActivityIndicator, Image } from "react-native"
import MyStyles from "../../Styles/MyStyles"
import React, { useEffect } from "react";
import API, { endpoints } from "../../Configs/API";
import Style from "./Style";

const LessonDetail = ({route}) => {
    const {lessonId} = route.params;
    const [lesson, setLesson] = React.useState(null);
    useEffect(() => {
        // chi tiết trả ra đối tượng
        const loadLesson = async()=>{
            try{
                let res = await API(endpoints['lesson-details'](lessonId));
                setLesson(res.data);
            }catch(ex){
                console.error(ex);
            }
        }
        loadLesson();
    },[lessonId])

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>CHI TIẾT BÀI HỌC</Text>

            {/* kiểm tra */}
            {lesson=== null?<ActivityIndicator/>:<>
                {/* đổ dữ liệu ra
                Mặc định trên điện thoại là dọc => gắn style row */}
                <View style={MyStyles.row}>
                    <Image style={Style.img}source={{uri: lesson.image}}/>
                    <View style={MyStyles.row}>
                        <Text style={MyStyles.subject}>{lesson.subject}</Text>
                    </View>
                </View>
            </>}
        </View>
    )
}

export default LessonDetail;