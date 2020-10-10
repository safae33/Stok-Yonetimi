<template>
  <v-row>
      
  </v-row>
</template>

<script>
import menu from "@/config/menu.json"
export default {
    name:"Menu",
    computed:{
        menuItems: () => {
            return menu.items
        }
    },
    data() {
        return{

        }
    }

}
</script>

<style>

</style>