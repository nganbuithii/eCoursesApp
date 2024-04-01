import { View, Text, ActivityIndicator, Image, ScrollView } from "react-native"
import MyStyles from "../../Styles/MyStyles"
import React, { useEffect } from "react";
import API, { endpoints } from "../../Configs/API";
import Style from "./Style";
import RenderHTML from 'react-native-render-html';
import moment from "moment";

const LessonDetail = ({route}) => {
    const {lessonId} = route.params;
    const [comments, setComment] = React.useState(null);
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
        const loadComment = async () => {
            try{
                let res = await API.get(endpoints['comments'](lessonId));
                setComment(res.data); // Cập nhật state comments với dữ liệu từ API
            }catch(ex){
                console.error(ex);
            }
        }
        
        loadLesson();
        loadComment();
    },[lessonId])

    return (
        <ScrollView>
            <View style={MyStyles.container}>
                <Text style={MyStyles.subject}>CHI TIẾT BÀI HỌC</Text>
                {lesson === null ? (
                    <ActivityIndicator/>
                ) : (
                    <>
                        <View style={MyStyles.row}>
                            <Image style={Style.img} source={{uri: lesson.image}}/>
                            <View>
                                <Text style={MyStyles.subject}>{lesson.subject}</Text>
                                <View style={MyStyles.row}>
                                    {lesson.tags.map(t => <Text style={Style.tag}>{t.name}</Text>)}
                                </View>
                            </View>
                        </View>
                        <View>
                            <RenderHTML source={{html: lesson.content}}/>
                        </View>
                    </>
                )}
            </View>
            {/* Hiển thị comments */}
            <ScrollView>
                {comments === null ? (
                    <ActivityIndicator/>
                ) : (
                    <>
                        {comments.map(c => (
                            <View style={Style.commentContainer} key={c.id}>
                                <View style={Style.commentHeader}>
                                    <Image style={Style.thumb} source={{uri: c.user.image}}/>
                                    <Text style={Style.commentUsername}>{c.user.username}</Text>
                                    <Text style={Style.commentDate}>{moment(c.create_date).format('DD/MM/YYYY')}</Text>
                                </View>
                                <View style={Style.commentContent}>
                                    <Text style={Style.commentText}>{c.content}</Text>
                                </View>
                            </View>
                        ))}

                    </>
                )}
            </ScrollView>
        </ScrollView>
        
    
        
    
    )
}

export default LessonDetail;