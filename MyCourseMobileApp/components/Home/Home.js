import { View, Text } from "react-native";
import MyStyle from "../../styles/MyStyle";
import Style from "./Style";

// component
const Home = () => {
    return(
        <View style={MyStyle.container}>
            <Text style={Style.subject}>HOME</Text>
        </View>
    )
}

export default Home;
