import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

// import { NavigationContainer } from '@react-navigation/native';
// import { createDrawerNavigator } from '@react-navigation/drawer';
// import Login from './components/User/Login';
// import Home from './components/Home/Home';

// const Drawer = createDrawerNavigator();
export default function App() {
  return (
    // <NavigationContainer>
    //         <Drawer.Navigator initialRouteName='Home'>
    //             <Drawer.Screen name="Home" component={Home} />
    //             <Drawer.Screen name="Login" component={Login} />
    //         </Drawer.Navigator>
    // </NavigationContainer>
    <View style={styles.container}>
        <Text style={styles.txt}>HELLO WORLD</Text>
        <StatusBar style="auto" />
    </View>
);

}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  txt:{
    color:"pink",
    fontSize:50,
    transform:[{rotate:"30deg"}]
  }
});
