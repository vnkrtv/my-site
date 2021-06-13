import bridge from '@vkontakte/vk-bridge';

bridge.send("VKWebAppInit", {});
bridge.send("VKWebAppGetUserInfo", {});
bridge.subscribe((e) => {
if(e.type === "VKWebAppGetUserInfo") {
   console.log(e.data.status);
   const title = document.getElementById('mainTitle');
   title.innerHTML = `Hello, ${e.data.first_name} ${e.data.second_name} from ${e.data.city.title}!`;
}});