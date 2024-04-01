import {NavigationContainer} from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer';
import { DrawerContentScrollView, DrawerItemList, DrawerItem } from '@react-navigation/drawer';

import Home from './components/Home/Home';
import Login from './components/User/Login';
import { useEffect, useState } from 'react';
import API, { endpoints } from './Configs/API';
import { ActivityIndicator } from 'react-native';
import Lesson from './components/lesson/lesson';

const Drawer = createDrawerNavigator();

// Điều hướng trên màn hình hải bọc trong NavigationContainer
const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator drawerContent={MyDrawerItem}>
        {/* gắn màn hình */}
        {/* Nạp API Danh mục DrawerContent*/}
        <Drawer.Screen name="Home" component={Home} options={{title:"Khóa học"}}/>
        <Drawer.Screen name='Login' component={Login} />
        <Drawer.Screen name='Lesson' component={Lesson} options={{title:"Bài học"}} />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

const MyDrawerItem = ({ navigation, ...props }) => { // Destructure navigation từ props
  //gọi API categories
  const [categories, setCategories] = useState(null);

  useEffect(() => {
    const loadCategories = async() =>{
      try{
        let res = await API.get(endpoints['categories']);
        setCategories(res.data)
      } catch(ex) {
        setCategories([])
        console.error(ex);
      }
    }
    loadCategories(); // Kích hoạt loadCategories khi component được mount
  },[])

  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props}/>

      {/* Kiểm tra nếu categories không null và không phải undefined */}
      {categories !== null && categories !== undefined ? (
        categories.map(c => (
          <DrawerItem
            key={c.id}
            label={c.name}
            onPress={() => navigation.navigate("Home", { "cateId": c.id })}
          />
        ))
      ) : (
        <ActivityIndicator /> // Hiển thị Indicator khi dữ liệu đang được tải
      )}
    </DrawerContentScrollView>
  )
}


export default App;











// import { StatusBar } from 'expo-status-bar';
// import React from 'react';
// import { StyleSheet, Text, View } from 'react-native';

// // import { NavigationContainer } from '@react-navigation/native';
// // import { createDrawerNavigator } from '@react-navigation/drawer';
// // import Login from './components/User/Login';
// // import Home from './components/Home/Home';

// // const Drawer = createDrawerNavigator();
// export default function App() {
//   return (
//     // <NavigationContainer>
//     //         <Drawer.Navigator initialRouteName='Home'>
//     //             <Drawer.Screen name="Home" component={Home} />
//     //             <Drawer.Screen name="Login" component={Login} />
//     //         </Drawer.Navigator>
//     // </NavigationContainer>
//     <View style={styles.container}>
//         <Text style={styles.txt}>HELLO WORLD</Text>
//         <StatusBar style="auto" />
//     </View>
// );

// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   txt:{
//     color:"pink",
//     fontSize:50,
//     transform:[{rotate:"30deg"}]
//   }
// });
