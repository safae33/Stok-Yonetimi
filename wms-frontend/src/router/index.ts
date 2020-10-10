import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    redirect: "/allApplies",
    component: () => import("@/views/Base.vue"),
    children: [
      {
        path: "/",
        name: "Ana Sayfa",
        component: () => import("@/components/dashboard/Dashboard.vue")
      },
      {
        path: "/allApplies",
        name: "Tüm Başvurular",
        component: () => import("@/components/AllAplies.vue")
      },
      {
        path: "/newApply",
        name: "Yeni Başvuru",
        component: () => import("@/components/NewApply.vue")
      },
      {
        path: "/allUsers",
        name: "Tüm Firmalar",
        component: () => import("@/components/user/AllUsers.vue")
      },
      {
        path: "/allProducts",
        name: "Tüm Ürünler",
        component: () => import("@/components/product/ProductListBase.vue")
      },
      {
        path: "/stock",
        name: "Aktif Stok Listesi",
        component: () => import("@/components/stock/StockList.vue")
      },
    ]
  },
  {
    path: "/auth",
    redirect: "/auth/login",
    component: () => import("@/views/Auth.vue"),
    children: [
      {
        path: "/auth/login",
        name: "Giriş Yap",
        component: () => import("@/components/auth/Login.vue")
      },
      {
        path: "/auth/register",
        name: "Üye Ol",
        component: () => import("@/components/auth/Register.vue")
      },
      {
        path: "/auth/forgetPassword",
        name: "Şifre Unuttum",
        component: () => import("@/components/auth/ForgetPassword.vue")
      },
    ]
  }
]

const router = new VueRouter({

  routes
})

export default router
