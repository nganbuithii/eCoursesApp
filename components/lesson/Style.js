import { StyleSheet } from "react-native"

export default StyleSheet.create({
    img:{
        width:100,
        height:100
    },
    tag:{
        width:85,
        height:30,
        backgroundColor:"pink",
        color:"red",
        padding:5,
        margin:5,
        borderRadius:10
    },
    thumb:{
        height:40,
        width:40,
        borderRadius:10
    },
    commentContainer: {
        flexDirection: 'column',
        padding: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#ccc',
    },
    commentHeader: {
        flexDirection: 'row',
        alignItems: 'center',
    },
    commentUsername: {
        marginLeft: 10,
        fontWeight: 'bold',
    },
    commentDate: {
        marginLeft: 'auto',
        color: '#999',
    },
    commentContent: {
        marginTop: 5,
    },
    commentText: {
        fontSize: 16,
    },
})