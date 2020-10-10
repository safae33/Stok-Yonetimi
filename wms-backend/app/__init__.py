from app.modules.wms.routes import wms  # auth nesnem aslında bir APIRouter.
from app.modules.auth.routes import auth  # auth nesnem aslında bir APIRouter.
from fastapi import FastAPI, APIRouter

# Init app
app = FastAPI()
appForPrefix = APIRouter()

######################################################################################################################
# AUTH modülünün router kısımlarını app e eklemek için.
appForPrefix.include_router(auth, prefix="/auth")
# Bu satırlar olmazsa benim uygulamamda auth ile alaklı hiçbir şey olmaz. birbirine bağlı modüllerle kontrol ederiz.
# Gerekli olanlar kullanıcı ne ister onu aynı uygulamadan yapabiliriz.
######################################################################################################################

######################################################################################################################
# AUTH modülünün router kısımlarını app e eklemek için.
appForPrefix.include_router(wms, prefix="/wms")
# Bu satırlar olmazsa benim uygulamamda auth ile alaklı hiçbir şey olmaz. birbirine bağlı modüllerle kontrol ederiz.
# Gerekli olanlar kullanıcı ne ister onu aynı uygulamadan yapabiliriz.
######################################################################################################################


app.include_router(appForPrefix, prefix="/api/v1")
