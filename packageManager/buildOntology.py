import subprocess

class Source:
  def __init__(self, uri, name):
    self.memberOf = 'Source'
    self.uri = uri
    self.name = name

class Package:
  def __init__(self):
    self.memberOf = 'Package'
    self.name = ''
    self.priority = ''
    self.section = ''
    self.installedSize = ''
    self.maintainer = ''
    self.architecture = ''
    self.version = ''
    self.replaces = ''
    self.provides = ''
    self.depends = ''
    self.conflicts = ''
    self.fileName = ''
    self.size = ''
    self.md5sum = ''
    self.sha1 = ''
    self.sha256 = ''
    self.sha512 = ''
    self.description = ''
    self.descriptionMd5 = ''
    self.homepage = ''
    self.source = ''

class Dependency:
  def __init__(self, packageOrigin, package, comparison, version):
    self.packageOrigin = packageOrigin
    self.package = package
    self.comparison = comparison
    self.version = version

class Database:
  def __init__(self):
    self.sources = []
    self.packages = []
    self.dependencyAtoms = []
    self.depends = []
    self.sourceNextId = 0
    self.packageNextId = 0
  
  def getSource(self, uri):
    for source in self.sources:
      if (source.uri == uri):
        return source

    source = Source(uri, 'Source__S' + str(len(self.sources) + 1))
    self.sources.append(source)
    return source

database = Database()
packagesName = []

print("Get all packages from sources list...")

# Get all packages from sources list
# subprocess.run("apt-cache search '' > temp.txt", shell=True)
f = open('temp.txt', 'r')
for line in f:
  packagesName.append(line.strip().split(' ')[0])
f.close()
print(str(len(packagesName)) + ' packages.')
#packagesName.append('discord')
#packagesName.append('google-chrome-stable')
#packagesName.append('warsaw')
count = 0

# Each package
for packageName in packagesName:
  count += 1
  #if count == 3:
  #  break

  # Get all versions and all packages in apt base
  output = subprocess.getoutput("{ (apt show " + packageName + " | grep 'APT-Sources: ') && echo '@@@' && apt-cache show " + packageName + "; }")
  outputSource, outputPackages = output.split('@@@')
  
  print('(' + str(count) + '/' + str(len(packagesName)) + ' - ' + str(round(count*100/len(packagesName), 2))+ '%) ' + packageName)

  # Get source
  source = ""
  for line in outputSource.split('\n'):
    if 'APT-Sources: ' in line.strip(): 
      for sourceBlock in line.strip().split(' '):
        if 'http' in sourceBlock:
          source = database.getSource(sourceBlock)

  # Get packages
  packageBlocks = outputPackages.split('\n\n')
  for packageBlock in packageBlocks:
    # Each package version
    package = Package()
    package.source = source
    lines = packageBlock.split('\n')  
    for line in lines:
      lineStrip = line.strip()
      if 'Package: ' in lineStrip:
        package.name = lineStrip.replace('Package: ', '')
      if 'Priority: ' in lineStrip:
        package.priority = lineStrip.replace('Priority: ', '')
      if 'Section: ' in lineStrip:
        package.section = lineStrip.replace('Section: ', '')
      if 'Installed-Size: ' in lineStrip:
        package.installedSize = lineStrip.replace('Installed-Size: ', '')
      if 'Maintainer: ' in lineStrip:
        package.maintainer = lineStrip.replace('Maintainer: ', '')
      if 'Architecture: ' in lineStrip:
        package.architecture = lineStrip.replace('Architecture: ', '')
      if 'Version: ' in lineStrip:
        package.version = lineStrip.replace('Version: ', '')
        print(' => ' + package.version)
      if 'Replaces: ' in lineStrip:
        package.replaces = lineStrip.replace('Replaces: ', '')
      if 'Provides: ' in lineStrip:
        package.provides = lineStrip.replace('Provides: ', '')
      if 'Depends: ' in lineStrip:
        package.depends = lineStrip.replace('Depends: ', '')
      if 'Conflicts: ' in lineStrip:
        package.conflicts = lineStrip.replace('Conflicts: ', '')
      if 'Filename: ' in lineStrip:
        package.fileName = lineStrip.replace('Filename: ', '')
      if 'Size: ' in lineStrip:
        package.size = lineStrip.replace('Size: ', '')
      if 'MD5sum: ' in lineStrip:
        package.md5sum = lineStrip.replace('MD5sum: ', '')
      if 'SHA1: ' in lineStrip:
        package.sha1 = lineStrip.replace('SHA1: ', '')
      if 'SHA256: ' in lineStrip:
        package.sha256 = lineStrip.replace('SHA256: ', '')
      if 'SHA512: ' in lineStrip:
        package.sha512 = lineStrip.replace('SHA512: ', '')
      if 'Description: ' in lineStrip:
        package.description = lineStrip.replace('Description: ', '')
      if 'Description-pt_BR: ' in lineStrip:
        package.description = lineStrip.replace('Description-pt_BR: ', '')
      if 'Description-md5: ' in lineStrip:
        package.descriptionMd5 = lineStrip.replace('Description-md5: ', '')
      if 'Description-md5: ' in lineStrip:
        package.descriptionMd5 = lineStrip.replace('Description-md5: ', '')
      if 'Homepage: ' in lineStrip:
        package.homepage = lineStrip.replace('Homepage: ', '')
    
    database.packages.append(package)
  
fileOntology = open('Packages.wsml', 'w')

fileOntology.write('// Variant\n')
fileOntology.write('wsmlVariant _"http://www.wsmo.org/wsml/wsml-syntax/wsml-rule"\n\n')

fileOntology.write('// Namespace\n')
fileOntology.write('namespace {\n')
fileOntology.write('\t_"br.com.devdaniellima/RepositoryOntology/Packages"\n')
fileOntology.write('}\n\n')

fileOntology.write('// Definition\n')
fileOntology.write('ontology Packages\n')
fileOntology.write('\tnfp\n')
fileOntology.write('\t\tdc#title hasValue "Repository Packages"\n')
fileOntology.write('\t\tdc#contributor hasValue "Daniel Lima"\n')
fileOntology.write('\t\tdc#date hasValue _date(2021,03,21)\n')
fileOntology.write('\t\tdc#format hasValue "text/plain"\n')
fileOntology.write('\t\tdc#language hasValue "en-US" \n')
fileOntology.write('\tendnfp\n\n')

fileOntology.write('importsOntology {\n')
fileOntology.write('\trp#Repository\n')
fileOntology.write('}\n\n')

fileOntology.write('// Sources instances\n')

for source in database.sources:
  fileOntology.write("instance " + source.name + " memberOf Source\n")
  fileOntology.write('\turi hasValue "' + source.uri + '"\n')

  fileOntology.write('\n')

fileOntology.write('// Packages instances\n')

count = 0
for package in database.packages:
  count += 1
  instanceName = package.name.replace('-','_').capitalize() + '__P' + str(count)
  fileOntology.write("instance " + instanceName + ' memberOf Package\n')
  
  fileOntology.write('\tpackage hasValue "' + package.name + '"\n')

  fileOntology.write('\tpackageSource hasValue ' + package.source.name + '\n')

  if package.priority != '' :
    fileOntology.write('\tpriority hasValue "' + package.priority + '"\n')

  if package.section != '' :
    fileOntology.write('\tsection hasValue "' + package.section + '"\n')

  if package.installedSize != '' :
    fileOntology.write('\tinstalledSize hasValue "' + package.installedSize + '"\n')

  if package.maintainer != '' :
    fileOntology.write('\tmaintainer hasValue "' + package.maintainer.replace('"', '\\"') + '"\n')

  if package.architecture != '' :
    fileOntology.write('\tarchitecture hasValue "' + package.architecture + '"\n')

  if package.version != '' :
    fileOntology.write('\tversion hasValue "' + package.version + '"\n')

  if package.replaces != '' :
    fileOntology.write('\treplaces hasValue "' + package.replaces + '"\n')

  if package.provides != '' :
    fileOntology.write('\tprovides hasValue "' + package.provides + '"\n')

  if package.depends != '' :
    fileOntology.write('\tdepends hasValue "' + package.depends + '"\n')
    dependsArrString = package.depends.split(',')
    for dependString in dependsArrString:
      depPackage = ""
      depComparison = ""
      depVersion = ""
      # Ignora casos com o OR
      firstDependencyAtom = dependString.split('|')[0].strip()
      firstDependencyAtomArr = firstDependencyAtom.split(' ')
      depPackage = firstDependencyAtomArr[0]
      if (len(firstDependencyAtomArr) > 1):
        depComparison = firstDependencyAtomArr[1]
        if depComparison[0] == "(":
          depComparison = depComparison[1:]
      if (len(firstDependencyAtomArr) > 2):
        depVersion = firstDependencyAtomArr[2]
        if depVersion[-1] == ")":
          depVersion = depVersion[:-1]
      database.dependencyAtoms.append(Dependency(instanceName, depPackage, depComparison, depVersion))

  if package.conflicts != '' :
    fileOntology.write('\tconflicts hasValue "' + package.conflicts + '"\n')

  if package.fileName != '' :
    fileOntology.write('\tfileName hasValue "' + package.fileName + '"\n')

  if package.size != '' :
    fileOntology.write('\tsize hasValue "' + package.size + '"\n')

  if package.md5sum != '' :
    fileOntology.write('\tmd5sum hasValue "' + package.md5sum + '"\n')

  if package.sha1 != '' :
    fileOntology.write('\tsha1 hasValue "' + package.sha1 + '"\n')

  if package.sha256 != '' :
    fileOntology.write('\tsha256 hasValue "' + package.sha256 + '"\n')

  if package.sha512 != '' :
    fileOntology.write('\tsha512 hasValue "' + package.sha512 + '"\n')

  if package.description != '' :
    fileOntology.write('\tdescription hasValue "' + package.description.replace('"', '\\"') + '"\n')

  if package.descriptionMd5 != '' :
    fileOntology.write('\tdescriptionMd5 hasValue "' + package.descriptionMd5.replace('"', '\\"') + '"\n')

  if package.homepage != '' :
    fileOntology.write('\thomepage hasValue "' + package.homepage.replace('"', '\\"') + '"\n')

  
  fileOntology.write('\n')

# dependencyAtoms instances
count = 0
fileOntology.write('// DependencyAtom instances\n')
for dependency in database.dependencyAtoms:
  count += 1
  instanceName = "DepAtom__" + str(count)
  fileOntology.write("instance " + instanceName + " memberOf DependencyAtom\n")
  fileOntology.write('\tpackage hasValue "' + dependency.package + '"\n')
  fileOntology.write('\tcomparison hasValue "' + dependency.comparison + '"\n')
  fileOntology.write('\tversion hasValue "' + dependency.version + '"\n')

  database.depends.append([dependency.packageOrigin, instanceName])

  fileOntology.write('\n')

# RelationInstances
fileOntology.write('// RelationInstances for depends \n')
for relIns in database.depends:
  fileOntology.write("relationInstance depends("+relIns[0] + ", " + relIns[1] + ")")

  fileOntology.write('\n')

fileOntology.close()